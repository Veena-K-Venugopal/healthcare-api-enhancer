from datetime import datetime, timezone
import hashlib
import os
from pathlib import Path
from typing import Optional
import json

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

#log writer function; appends one JSONL event to log file
def log_prediction_event(
        *,
        request_id: str,
        input_text: str,
        prediction: str,
        model_version: str,
        latency_ms: int,
        cached: bool = False,
        error: Optional[str] = None,
) -> None:
    """
    Append one JSONL event to a local file.

    PII-safe by design:
    - does NOT store raw input_text
    - stores only length + sha256 hash
    """
    record = {
        "ts": _utc_iso(),
        "request_id": request_id,
        "input_length": len(input_text),
        "input_hash": _sha256(input_text),
        "prediction": prediction,
        "model_version": model_version,
        "latency_ms": latency_ms,
        "cached": cached,
    }

    if error:
        record["error"] = error

    log_path = _get_log_path()
    log_path.parent.mkdir(parents=True, exist_ok=True)

    with log_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")