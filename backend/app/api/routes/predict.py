from fastapi import APIRouter
import time
import uuid

from app.logging.prediction_logger import log_prediction_event
from app.api.schemas.predict import PredictRequest, PredictResponse
from app.ml.state import get_model

router = APIRouter(prefix="/predict", tags=["predict"])

@router.post("", response_model=PredictResponse)
def predict(request: PredictRequest):
    request_id = uuid.uuid4().hex[:8]
    start = time.perf_counter()

    model = get_model()

    prediction = "placeholder"

    latency_ms = int((time.perf_counter() - start) * 1000)

    log_prediction_event(
        request_id=request_id,
        input_text=request.text,
        prediction=prediction,
        model_version=model["version"],
        latency_ms=latency_ms,
        cached=False,
    )

    return PredictResponse(
        prediction=prediction,
        model_version=model["version"],
    )