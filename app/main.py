import os
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    environment = os.getenv("ENVIRONMENT", "development")
    api_key = os.getenv("MY_API_KEY")
    return {
        "message": "Hello CI/CD",
        "environment": environment
    }