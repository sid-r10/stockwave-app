from fastapi import FastAPI
from app.api.api import api_router

app = FastAPI(title="StockWave.ai API")
app.include_router(api_router)

@app.get("/")
# def health_check():
#     return {"status": "StockWave backend is running 🚀"}

def welcome():
    return {
        "message": "👋 Welcome to StockWave.ai API",
        "status": "running",
        "version": "1.0.0"
    }