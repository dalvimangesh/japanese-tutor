import pytest
from server import app
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_serve_index(client):
    """Test the index page endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    assert response.mimetype == 'text/html'

def test_hello_world_post(client):
    """Test the POST endpoint that generates random Japanese sentence"""
    response = client.post('/')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'message' in data
    assert isinstance(data['message'], str)

def test_health(client):
    """Test the health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'OK'

def test_submit_text(client):
    """Test the submit text endpoint"""
    test_text = "こんにちは"
    response = client.post('/submit',
                          json={'text': test_text},
                          content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'message' in data
    assert isinstance(data['message'], str)

def test_submit_text_empty(client):
    """Test the submit text endpoint with empty text"""
    response = client.post('/submit',
                          json={'text': ''},
                          content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'message' in data
    assert isinstance(data['message'], str)

def test_submit_text_missing_text(client):
    """Test the submit text endpoint with missing text field"""
    response = client.post('/submit',
                          json={},
                          content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'message' in data
    assert isinstance(data['message'], str)

def test_serve_css(client):
    """Test the CSS file serving endpoint"""
    response = client.get('/styles.css')
    assert response.status_code == 200
    assert response.mimetype == 'text/css' 