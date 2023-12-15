from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_hello_world():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "status": "Hello, world"
    }

def test_get_video_list():
    response = client.get("/moviereviews/Harry_Potter")
    assert response.status_code == 200
    reviews_list = response.json()

    assert len(reviews_list) == 10  
    
    for review in reviews_list:
        assert not review['id'] == None
        assert not review['title'] == None
        assert not review['description'] == None

    assert "Harry Potter".upper() in str(reviews_list).upper()