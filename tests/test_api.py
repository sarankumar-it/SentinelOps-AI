from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
def test_predict():
    payload = {
        "cpu_usage": 90,
        "memory_usage": 88,
        "response_time": 420,
        "error_rate": 0.15,
        "request_rate": 500
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200
    assert response.json()["risk"] == "High"
    assert "analysis" in response.json()

def test_invalid_cpu():
    payload = {
        "cpu_usage": 150,
        "memory_usage": 50,
        "response_time": 150,
        "error_rate": 0.05,
        "request_rate": 200
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 422
