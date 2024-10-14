from fastapi.testclient import TestClient

def test_chat_with_mistral_ok():
    from app.api.routes.chat import router
    client = TestClient(router)
    response = client.post("/chat", json={"message": "Hello"})
    assert response.status_code == 200
    

def test_chat_with_mistral_empty():
    from app.api.routes.chat import router
    client = TestClient(router)
    try:
        client.post("/chat", json={"message": ""})
    except Exception as e:
        assert e.status_code == 400