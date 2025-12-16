from fastapi import FastAPI

app = FastAPI(title="Healthcare API Enhancer")

@app.get("/health")
def health():
    return {"status": "ok"}