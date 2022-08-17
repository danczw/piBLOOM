from pibloom import __version__
from pibloom.app import app
import json

def test_version():
    assert __version__ == '0.1.0'

def test_index():
    tester = app.test_client()
    response = tester.get('/index/', content_type='html/text')
    
    assert response.status_code == 200
    assert b'Hello World!' in response.data

def test_index():
    tester = app.test_client()
    data = {'content':'This is a test'}
    response = tester.post('/chat/', data=json.dumps(data), content_type='application/json')
    
    assert response.status_code == 200