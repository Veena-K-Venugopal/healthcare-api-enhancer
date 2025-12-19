from datetime import datetime, timezone
import hashlib
import os
from pathlib import Path

DEFAULT_LOG_PATH = "backend/logs/predictions.jsonl"

# utc timestamp helper; returns current utc timestamp as string
def _utc_iso() -> str:
    return datetime.now(timezone.utc).isoformat()

# sha-256 hash helper; returns sha-256 hash of input string as hexadecimal string
def _sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

# file path helper; returns log file path as pathlib.Path object
def _get_log_path() -> Path:
    return Path(os.getenv("PREDICT_LOG_PATH", DEFAULT_LOG_PATH))
