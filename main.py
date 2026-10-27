from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(title="Cloud Deployment API - Level 4")

@app.get("/")
def health_check():
    return {
        "status": "online",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "message": "The server is running smoothly inside the Docker container!"
    }

