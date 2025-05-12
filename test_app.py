from app import app

def test_home():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Flask App!" in response.data

def test_get_items():
    tester = app.test_client()
    response = tester.get('/items')
    assert response.status_code == 200
