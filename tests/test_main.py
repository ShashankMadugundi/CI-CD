from fastapi.testclient import TestClient

from app.main import app
import os

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello CI/CD",
        "environment": "test"
    }
    
def test_api_key_exists():
    assert os.getenv("MY_API_KEY") is not None