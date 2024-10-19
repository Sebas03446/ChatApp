from fastapi.testclient import TestClient
from app.core.config.database import Session, Base, engine
import pytest
from app.api.routes.chat import router
from app.api.models.specialization import Specialization
from unittest.mock import patch
import json




@pytest.fixture(scope="module")
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_chat_with_mistral_ok():
    client = TestClient(router)
    mock_get_chat_response = patch("app.api.routes.chat.get_chat_response").start()
    mock_get_chat_response.return_value = json.dumps({"status_code": 200, "response": "Hello"})
    
    response = client.post("/chat", json={"message": "Hello"})
    assert response.status_code == 200
    

def test_chat_with_mistral_empty():
    client = TestClient(router)
    try:
        client.post("/chat", json={"message": ""})
    except Exception as e:
        assert e.status_code == 400
        
def test_chat_with_mistral_specialization_not_found(setup_database):
    client = TestClient(router)
    try:
        client.post("/chat", json={"message": "Hello", "specialization": "AI"})
    except Exception as e:
        assert e.status_code == 404

def test_chat_with_mistral_specialization_found(setup_database):
    client = TestClient(router)
    mock_get_chat_response = patch("app.api.routes.chat.get_chat_response").start()
    mock_get_chat_response.return_value = json.dumps({"message": "Hello", "specialization": "Mistral_traduction"})

    db = Session()
    db.add(Specialization(name="Mistral_traduction", description="Mistral Specialization", initialPrompt="Hi you are a professional translator"))
    db.commit()

    response = client.post("/chat", json={"message": "Hello", "specialization": "Mistral_traduction"})
    assert response.status_code == 200
    assert response.json()["message"] == "Hello"
    assert response.json()["specialization"] == "Mistral_traduction"