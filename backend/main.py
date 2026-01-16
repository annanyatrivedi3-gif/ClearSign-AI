from fastapi import FastAPI
from backend.api.analyze import router as analyze_router

app = FastAPI(title="ClearSign AI")

app.include_router(analyze_router)

@app.get("/")
def health():
    return {"status": "ClearSign AI backend running"}
