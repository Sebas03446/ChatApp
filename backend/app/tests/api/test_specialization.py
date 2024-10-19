from fastapi.testclient import TestClient
from app.api.routes.specialization import router
from app.core.config.database import Base, test_engine
import pytest

client = TestClient(router)

@pytest.fixture(scope="module")
def setup_database():
    Base.metadata.create_all(bind=test_engine)
    yield
    Base.metadata.drop_all(bind=test_engine)

def test_create_specialization_ok(setup_database):
    response = client.post("/specialization", json={
        "name": "AI",
        "description": "Artificial Intelligence",
        "initialPrompt": "What is AI?"
    })
    assert response.status_code == 200
    assert response.json() == {
        "name": "AI",
        "description": "Artificial Intelligence",
        "initialPrompt": "What is AI?"
    }

def test_create_specialization_empty_name(setup_database):
    try:
        response = client.post("/specialization", json={
            "name": "",
            "description": "Artificial Intelligence",
            "initialPrompt": "What is AI?"
        })
    except Exception as e:
        assert e.status_code == 400
        assert e.detail == "Name cannot be empty"

def test_get_specializations(setup_database):
    response = client.get("/specialization")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_specialization(setup_database):
    response = client.get("/specialization/AI")
    assert response.status_code == 200
    assert response.json()["name"] == "AI"

def test_update_specialization(setup_database):
    response = client.put("/specialization/AI", json={
        "name": "AI Updated",
        "description": "Artificial Intelligence Updated",
        "initialPrompt": "What is AI Updated?"
    })
    assert response.status_code == 200
    assert response.json() == {
        "name": "AI Updated",
        "description": "Artificial Intelligence Updated",
        "initialPrompt": "What is AI Updated?"
    }

def test_delete_specialization(setup_database):
    response = client.delete("/specialization/AI Updated")
    assert response.status_code == 200
    assert response.json() == {"name": "AI Updated", "status": "deleted"}