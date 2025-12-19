from datetime import datetime, timezone
import hashlib

# utc timestamp helper; returns current utc timestamp as string
def _utc_iso() -> str:
    return datetime.now(timezone.utc).isoformat()

# sha-256 hash helper; returns sha-256 hash of input string as hexadecimal string
def _sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()
