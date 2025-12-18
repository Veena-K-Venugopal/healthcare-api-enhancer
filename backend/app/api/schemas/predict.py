from pydantic import BaseModel, Field

class PredictRequest(BaseModel):
    text: str = Field(...,min_length=1, description="Input text for prediction")

class PredictResponse(BaseModel):
    prediction: str
    model_version: str