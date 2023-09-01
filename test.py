from inventory.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_add_task():
    # Test adding a task
    task_data = {"id": 1, "name": "Buy groceries", "price": 100,"quantity":100}
    response = client.post("/products/", json=task_data)
    assert response.status_code == 200
    task_response = response.json()
    assert "id" in task_response
    assert task_response["id"] == task_data["id"]
    assert task_response["name"] == task_data["name"]
    assert task_response["price"] == task_data["price"]
    assert task_response["quantity"] == task_data["quantity"]



def test_get_task():
    # Test getting tasks
    response = client.get("/products/")
    assert response.status_code == 200
    assert response.json() == []

    task_data = {"id": 1, "name": "Buy groceries", "price": 100,"quantity":100}
    client.post("/products/", json=task_data)
    response = client.get("/products/")
    assert response.status_code == 200

    tasks_response = response.json()
    assert len(tasks_response) == 1
    assert "id" in tasks_response[0]
    assert tasks_response[0]["id"] == task_data["id"]
    assert tasks_response[0]["name"] == task_data["name"]
    assert tasks_response[0]["price"] == task_data["price"]
    assert tasks_response[0]["quantity"] == task_data["quantity"]

    print(tasks_response )