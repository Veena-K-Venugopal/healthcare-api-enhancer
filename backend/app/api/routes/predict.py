from fastapi import APIRouter

from app.api.schemas.predict import PredictRequest, PredictResponse
from app.ml.state import get_model

router = APIRouter(prefix="/predict", tags=["predict"])

@router.post("", response_model=PredictResponse)
def predict(request: PredictRequest):
    model = get_model()

    return PredictResponse(
        prediction="placeholder",
        model_version=model["version"],
    )