from fastapi.testclient import TestClient
from main import app
from articles_router import articles

client = TestClient(app)

def test_get_articles():
    response = client.get("/articles/")
    assert response.status_code == 200
    assert response.json() == articles

def test_add_article():
    response = client.post("/articles/", json={"id": 1, "title": "New Article", "content": "Content of the article"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "title": "New Article", "content": "Content of the article"}

def test_delete_article():
    client.post("/articles/", json={"id": 2, "title": "Another Article", "content": "Content of another article"})
    delete_response = client.delete("/articles/2")
    assert delete_response.status_code == 204
    assert not any(article for article in articles if article.id == 2)
