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
    # Download activity slots. Each host still gets one request in flight (http._in_flight)
    # spaced >= 1.1 s apart; extra slots only let cache hits and other hosts proceed while
    # a slow RDS response is pending. OEB_DOWNLOAD_SLOTS=0 pauses crawling: download tasks
    # wait in Temporal while parse/embed keep running.
    download_slots = int(os.environ.get("OEB_DOWNLOAD_SLOTS", "3"))
    workers = [
        Worker(client, task_queue=TASK_QUEUE, workflows=[IngestCaseWorkflow, IngestDocWorkflow],
               activities=[activities.register_case]),
        Worker(client, task_queue=CPU_QUEUE,
               activities=[activities.parse, activities.embed, activities.refresh_search_stats],
               max_concurrent_activities=2),
    ]
    if download_slots > 0:
        workers.append(Worker(client, task_queue=DOWNLOAD_QUEUE, activities=[activities.download],
                              max_concurrent_activities=download_slots))
    print(f"worker on {TEMPORAL_ADDRESS} queues={TASK_QUEUE},{DOWNLOAD_QUEUE},{CPU_QUEUE}", flush=True)
    await asyncio.gather(*(w.run() for w in workers))


if __name__ == "__main__":
    asyncio.run(main())
