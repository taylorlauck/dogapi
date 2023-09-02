import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

def test_home_route(client):
    response = client.get('/')
    assert b'Please enter your name' in response.data

def test_home_with_name_route(client):
    response = client.get('/home/John')
    assert b'John please select the dog you want to see' in response.data

def test_invalid_home_with_name_route(client):
    response = client.get('/home/')
    assert response.status_code == 404



