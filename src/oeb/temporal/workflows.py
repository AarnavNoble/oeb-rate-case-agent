"""IngestCaseWorkflow lists a case, then runs one IngestDocWorkflow per document
(download -> parse+chunk -> embed). Every activity is idempotent on documents.status,
so re-running the workflow skips finished documents."""

import asyncio
from datetime import timedelta

from temporalio import workflow
from temporalio.common import RetryPolicy
from temporalio.exceptions import ActivityError, ChildWorkflowError

with workflow.unsafe.imports_passed_through():
    from oeb.config import CPU_QUEUE, DOWNLOAD_QUEUE
    from oeb.temporal import activities

RETRY = RetryPolicy(initial_interval=timedelta(seconds=10), backoff_coefficient=2.0,
                    maximum_interval=timedelta(minutes=5), maximum_attempts=5,
                    non_retryable_error_types=["ParseError"])


@workflow.defn
class IngestDocWorkflow:
    @workflow.run
    async def run(self, doc_id: str) -> dict:
        out: dict = {"doc_id": doc_id}
        # network-bound and CPU-bound work run on separate queues with separate slot limits,
        # so slow downloads never block parsing of files that are already on disk
        out["download"] = await workflow.execute_activity(
            activities.download, doc_id, task_queue=DOWNLOAD_QUEUE,
            start_to_close_timeout=timedelta(minutes=15), heartbeat_timeout=activities.HEARTBEAT_TIMEOUT,
            retry_policy=RETRY)
        out["parse"] = await workflow.execute_activity(
            activities.parse, doc_id, task_queue=CPU_QUEUE,
            start_to_close_timeout=timedelta(minutes=60), heartbeat_timeout=activities.HEARTBEAT_TIMEOUT,
            retry_policy=RETRY)
        out["embed"] = await workflow.execute_activity(
            activities.embed, doc_id, task_queue=CPU_QUEUE,
            start_to_close_timeout=timedelta(minutes=60), heartbeat_timeout=activities.HEARTBEAT_TIMEOUT,
            retry_policy=RETRY)
        return out


@workflow.defn
class IngestCaseWorkflow:
    @workflow.run
    async def run(self, case: str) -> dict:
        doc_ids = await workflow.execute_activity(
            activities.register_case, case, start_to_close_timeout=timedelta(minutes=30), retry_policy=RETRY)

        async def one(doc_id: str) -> dict:
            try:
                return await workflow.execute_child_workflow(
                    IngestDocWorkflow.run, doc_id, id=f"ingest-doc-{doc_id}")
            except ChildWorkflowError as e:
                cause = e.cause.cause if isinstance(e.cause, ActivityError) else e.cause
                return {"doc_id": doc_id, "failed": str(cause or e)}

        results = await asyncio.gather(*(one(d) for d in doc_ids))
        failed = [r for r in results if "failed" in r]
        # corpus changed: recompute lexeme document frequencies used by full-text search
        stats = await workflow.execute_activity(
            activities.refresh_search_stats, task_queue=CPU_QUEUE,
            start_to_close_timeout=timedelta(minutes=10), retry_policy=RETRY)
        return {"case": case, "documents": len(doc_ids), "failed": failed, "search_stats": stats}
