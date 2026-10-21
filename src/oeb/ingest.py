"""Start (or re-run) the ingestion workflow for a case and wait for the result.

    uv run python -m oeb.ingest EB-2023-0195
"""

import asyncio
import json
import sys
import time

from temporalio.client import Client
from temporalio.common import WorkflowIDConflictPolicy, WorkflowIDReusePolicy

from oeb.config import TASK_QUEUE, TEMPORAL_ADDRESS
from oeb.temporal.workflows import IngestCaseWorkflow


async def main(case: str) -> None:
    client = await Client.connect(TEMPORAL_ADDRESS)
    t0 = time.time()
    # attach to a run already in progress (e.g. after this client was restarted); otherwise
    # start a new one, which skips documents that are already done
    handle = await client.start_workflow(
        IngestCaseWorkflow.run, case, id=f"ingest-{case}", task_queue=TASK_QUEUE,
        id_reuse_policy=WorkflowIDReusePolicy.ALLOW_DUPLICATE,
        id_conflict_policy=WorkflowIDConflictPolicy.USE_EXISTING)
    print(f"workflow {handle.id} run {handle.result_run_id}", file=sys.stderr, flush=True)
    result = await handle.result()
    result["wall_s"] = round(time.time() - t0, 1)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1]))
