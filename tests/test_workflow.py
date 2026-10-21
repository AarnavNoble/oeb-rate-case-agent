"""IngestCaseWorkflow with mocked activities on Temporal's time-skipping test server."""

import asyncio
import uuid

import pytest
from temporalio import activity
from temporalio.exceptions import ApplicationError
from temporalio.testing import WorkflowEnvironment
from temporalio.worker import Worker

from oeb.config import CPU_QUEUE, DOWNLOAD_QUEUE, TASK_QUEUE
from oeb.temporal.workflows import IngestCaseWorkflow, IngestDocWorkflow

calls: list[tuple[str, str]] = []


@activity.defn(name="register_case")
async def register_case(case: str) -> list[str]:
    return ["good", "unparseable", "flaky"]


@activity.defn(name="download")
async def download(doc_id: str) -> dict:
    calls.append(("download", doc_id))
    if doc_id == "flaky" and sum(1 for c in calls if c == ("download", "flaky")) < 3:
        raise RuntimeError("connection reset")  # retried by the workflow's retry policy
    return {"doc_id": doc_id}


@activity.defn(name="parse")
async def parse(doc_id: str) -> dict:
    calls.append(("parse", doc_id))
    if doc_id == "unparseable":
        raise ApplicationError("bad pdf", type="ParseError", non_retryable=True)
    return {"doc_id": doc_id}


@activity.defn(name="embed")
async def embed(doc_id: str) -> dict:
    calls.append(("embed", doc_id))
    return {"doc_id": doc_id}


@activity.defn(name="refresh_search_stats")
async def refresh_search_stats() -> dict:
    calls.append(("refresh", ""))
    return {"lexemes": 1}


def test_ingest_case_isolates_failures_and_retries():
    async def run() -> dict:
        calls.clear()
        async with await WorkflowEnvironment.start_time_skipping() as env:
            workers = [
                Worker(env.client, task_queue=TASK_QUEUE, workflows=[IngestCaseWorkflow, IngestDocWorkflow],
                       activities=[register_case]),
                Worker(env.client, task_queue=DOWNLOAD_QUEUE, activities=[download]),
                Worker(env.client, task_queue=CPU_QUEUE, activities=[parse, embed, refresh_search_stats]),
            ]
            async with workers[0], workers[1], workers[2]:
                return await env.client.execute_workflow(
                    IngestCaseWorkflow.run, "EB-TEST", id=f"t-{uuid.uuid4()}", task_queue=TASK_QUEUE)

    try:
        result = asyncio.run(run())
    except RuntimeError as e:  # test server binary unavailable (offline)
        pytest.skip(f"Temporal test server unavailable: {e}")

    assert result["documents"] == 3
    assert [f["doc_id"] for f in result["failed"]] == ["unparseable"]
    assert "bad pdf" in result["failed"][0]["failed"]
    assert ("embed", "good") in calls and ("embed", "flaky") in calls
    assert ("embed", "unparseable") not in calls          # non-retryable parse error stops that doc only
    assert sum(1 for c in calls if c == ("parse", "unparseable")) == 1  # and isn't retried
    assert sum(1 for c in calls if c == ("download", "flaky")) == 3     # transient errors are
    assert calls[-1] == ("refresh", "")                   # stats refresh runs after all documents
