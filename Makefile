.PHONY: up check ingest eval

# Postgres + Temporal dev server + ingest worker + API + web UI
up:
	uv run honcho start

check:
	uv run ruff check src evals tests && uv run pyright && uv run pytest -q

ingest:
	uv run python -m oeb.ingest $(CASE)

eval:
	uv run python -m evals.run
