import asyncio
import os

import psycopg
from temporalio.client import Client
from temporalio.worker import Worker

from oeb.config import CPU_QUEUE, DOWNLOAD_QUEUE, TASK_QUEUE, TEMPORAL_ADDRESS
from oeb.db import init_schema
from oeb.temporal import activities
from oeb.temporal.workflows import IngestCaseWorkflow, IngestDocWorkflow


async def _connect(retries: int = 60) -> Client:
    # `make up` starts the Temporal dev server alongside this worker
    for i in range(retries):
        try:
            return await Client.connect(TEMPORAL_ADDRESS)
        except RuntimeError:
            if i == retries - 1:
                raise
            await asyncio.sleep(2)
    raise AssertionError("unreachable")


async def main() -> None:
    for i in range(60):  # Postgres may still be starting under `make up`
        try:
            init_schema()
            break
        except psycopg.OperationalError:
            if i == 59:
                raise
            await asyncio.sleep(2)
    client = await _connect()
    workers = [
        Worker(client, task_queue=TASK_QUEUE, workflows=[IngestCaseWorkflow, IngestDocWorkflow],
               activities=[activities.register_case]),
        # downloads in flight (default 1: with 3, RDS started resetting connections); http.py also
        # spaces request starts >= 1.1 s apart per host
        Worker(client, task_queue=DOWNLOAD_QUEUE, activities=[activities.download],
               max_concurrent_activities=int(os.environ.get("OEB_DOWNLOAD_SLOTS", "1"))),
        Worker(client, task_queue=CPU_QUEUE,
               activities=[activities.parse, activities.embed, activities.refresh_search_stats],
               max_concurrent_activities=2),
    ]
    print(f"worker on {TEMPORAL_ADDRESS} queues={TASK_QUEUE},{DOWNLOAD_QUEUE},{CPU_QUEUE}", flush=True)
    await asyncio.gather(*(w.run() for w in workers))


if __name__ == "__main__":
    asyncio.run(main())
