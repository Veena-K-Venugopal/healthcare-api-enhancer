from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.ml.loader import load_model
from app.ml.state import set_model

@asynccontextmanager
async def lifespan(app: FastAPI):
    model = load_model()
    set_model(model)
    yield

app = FastAPI(title="Healthcare API Enhancer", lifespan=lifespan)

@app.get("/health")
def health():
    return {"status": "ok"}