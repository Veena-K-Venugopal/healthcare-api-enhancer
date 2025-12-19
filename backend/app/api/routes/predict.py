from fastapi import APIRouter
import time
import uuid

from app.api.schemas.predict import PredictRequest, PredictResponse
from app.ml.state import get_model

router = APIRouter(prefix="/predict", tags=["predict"])

@router.post("", response_model=PredictResponse)
def predict(request: PredictRequest):
    request_id = uuid.uuid4().hex[:8]
    start = time.perf_counter()

    model = get_model()

    return PredictResponse(
        prediction="placeholder",
        model_version=model["version"],
    )