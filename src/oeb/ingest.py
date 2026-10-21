"""Start (or re-run) the ingestion workflow for a case and wait for the result.

    uv run python -m oeb.ingest EB-2023-0195
"""

import asyncio
import json
import sys
import time

from temporalio.client import Client
from temporalio.common import WorkflowIDReusePolicy

from oeb.config import TASK_QUEUE, TEMPORAL_ADDRESS
from oeb.temporal.workflows import IngestCaseWorkflow


async def main(case: str) -> None:
    client = await Client.connect(TEMPORAL_ADDRESS)
    t0 = time.time()
    result = await client.execute_workflow(
        IngestCaseWorkflow.run, case, id=f"ingest-{case}", task_queue=TASK_QUEUE,
        id_reuse_policy=WorkflowIDReusePolicy.ALLOW_DUPLICATE)
    result["wall_s"] = round(time.time() - t0, 1)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1]))
