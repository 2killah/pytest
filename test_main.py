from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Salem"}

def test_sum():
    response = client.get("/sum?a=5&b=7")
    assert response.status_code == 200
    assert response.json() == {"result": 12}

def test_multiply():
    response = client.get("/multiply?a=2&b=8")
    assert response.status_code == 200
    assert response.json() == {"result": 16}

def test_ping():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}