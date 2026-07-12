from fastapi import FastAPI

app = FastAPI(
    title="Zero Cloud Storage",
    version="1.0.0"
)

@app.get("/health", tags=["System"])
async def health_check():
    """Эндпоинт для проверки того, что сервер жив."""
    return {"status": "ok", "message": "Zero API is running perfectly"}