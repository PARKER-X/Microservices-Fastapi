from inventory.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_read_main():
    response = client.get("/products")
    assert response.status_code == 200
    assert response.json() == {"id": id,"name":"Billy","price":100,"quantity":100}

