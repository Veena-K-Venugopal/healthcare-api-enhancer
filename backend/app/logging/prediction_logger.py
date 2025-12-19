from datetime import datetime, timezone

# utc timestamp helper; returns current utc timestamp as string
def _utc_iso() -> str:
    return datetime.now(timezone.utc).isoformat()