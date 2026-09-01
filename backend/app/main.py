from fastapi import FastAPI


app = FastAPI(
    title="SmartTrafficAI API",
    description="AI-powered traffic monitoring backend",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {
        "message": "SmartTrafficAI API is running",
        "version": "0.1.0",
    }


@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "service": "backend",
    }