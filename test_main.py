import pytest
from main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_joke(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert "joke" in data
    assert data["joke"] == "Why don't skeletons fight each other? They don't have the guts."