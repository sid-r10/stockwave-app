from fastapi import FastAPI

app = FastAPI(title="StockWave.ai API")

@app.get("/")
# def health_check():
#     return {"status": "StockWave backend is running 🚀"}

def welcome():
    return {
        "message": "👋 Welcome to StockWave.ai API",
        "status": "running",
        "version": "1.0.0"
    }