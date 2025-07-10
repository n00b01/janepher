from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "service": "janepher-backend"}

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Janepher" in response.json()["message"]
