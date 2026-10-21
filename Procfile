db: docker compose up db
temporal: temporal server start-dev --db-filename data/temporal.db --log-level warn
worker: uv run python -m oeb.temporal.worker
api: uv run uvicorn oeb.api:app --port 8077
web: npm --prefix web run dev -- --port 3077
