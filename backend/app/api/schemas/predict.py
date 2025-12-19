from pydantic import BaseModel, Field, field_validator

class PredictRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        max_length=5000, 
        description="Input text for prediction")
    @field_validator("text", mode="before")
    def normalize_and_validate_text(cls, v: str) -> str:
        if not isinstance(v, str):
            raise ValueError("text must be a string")
        
        v = v.strip()
        if not v:
            raise ValueError("text must not be empty or whitespace")
        
        return v

class PredictResponse(BaseModel):
    prediction: str
    model_version: str