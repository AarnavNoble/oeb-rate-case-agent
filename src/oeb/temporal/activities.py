"""Thin Temporal wrappers around the idempotent pipeline stages.

Each stage runs in a thread while the activity heartbeats, so a crashed or restarted
worker is detected within HEARTBEAT_TIMEOUT instead of the full start-to-close timeout."""

import asyncio
from collections.abc import Callable
from datetime import timedelta
from typing import Any

from temporalio import activity
from temporalio.exceptions import ApplicationError

from oeb import pipeline

HEARTBEAT_TIMEOUT = timedelta(seconds=60)


async def _run_with_heartbeat(fn: Callable[..., Any], *args: Any) -> Any:
    task = asyncio.create_task(asyncio.to_thread(fn, *args))
    while True:
        done, _ = await asyncio.wait({task}, timeout=10)
        if done:
            return task.result()
        activity.heartbeat()


@activity.defn
async def register_case(case: str) -> list[str]:
    return await asyncio.to_thread(pipeline.register_case, case)


@activity.defn
async def download(doc_id: str) -> dict:
    # one HTTP attempt per activity attempt; Temporal's retry policy does the backoff
    return await _run_with_heartbeat(pipeline.download_doc, doc_id, 1)


@activity.defn
async def parse(doc_id: str) -> dict:
    try:
        return await _run_with_heartbeat(pipeline.parse_doc, doc_id)
    except pipeline.ParseError as e:
        raise ApplicationError(str(e), type="ParseError", non_retryable=True) from e


@activity.defn
async def embed(doc_id: str) -> dict:
    return await _run_with_heartbeat(pipeline.embed_doc, doc_id)


@activity.defn
async def refresh_search_stats() -> dict:
    return await asyncio.to_thread(pipeline.refresh_search_stats)
