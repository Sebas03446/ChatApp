from fastapi.testclient import TestClient
from app.core.config import settings
 

def test_read_root():
    from app.api.routes.hello_world import router
    client = TestClient(router)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_read_item():
    from app.api.routes.hello_world import router
    client = TestClient(router)
    response = client.get("/items/5?q=somequery")
    assert response.status_code == 200
    assert response.json() == {"item_id": 5, "q": "somequery"}