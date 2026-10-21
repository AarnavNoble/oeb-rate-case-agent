import os
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[2]
load_dotenv(ROOT / ".env")

DATA_RAW = Path(os.environ.get("OEB_DATA_RAW", ROOT / "data" / "raw"))
DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://oeb:oeb@localhost:5433/oeb")
# role with SELECT on the agent_* views only (see schema.sql)
AGENT_DATABASE_URL = os.environ.get("AGENT_DATABASE_URL", "postgresql://agent_ro:agent_ro@localhost:5433/oeb")
TEMPORAL_ADDRESS = os.environ.get("TEMPORAL_ADDRESS", "localhost:7233")
TASK_QUEUE = "oeb-ingest"          # workflows + register_case
DOWNLOAD_QUEUE = "oeb-download"    # network-bound
CPU_QUEUE = "oeb-cpu"              # parse / chunk / embed

USER_AGENT = os.environ.get(
    "OEB_USER_AGENT",
    "oeb-ratecase-research/0.1 (portfolio research crawler; max 1 req/s; caches all downloads)",
)
MIN_REQUEST_INTERVAL_S = 1.1

EMBED_MODEL = "BAAI/bge-small-en-v1.5"
EMBED_DIM = 384
# bge v1.5 model card: prefix queries (not passages) for retrieval
EMBED_QUERY_PREFIX = "Represent this sentence for searching relevant passages: "

AGENT_MODEL = os.environ.get("OEB_AGENT_MODEL", "claude-sonnet-5-5")
