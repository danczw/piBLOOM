from fastapi.testclient import TestClient
from pibloom import __version__
from pibloom.app import app
import json

client = TestClient(app)

def test_version():
    assert __version__ == '0.1.0'

def test_root():
    response = client.get('/')
    
    assert response.status_code == 200
    assert response.json() == {'data': 'Hello World!'}

def test_index():
    data = {'content':'This is a test'}
    response = client.post('/chat/', data=json.dumps(data))
    
    assert response.status_code == 200