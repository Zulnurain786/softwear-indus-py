"""
Flask application tests.
"""

import pytest
from app import app

@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test home page."""
    response = client.get('/home')
    assert response.status_code == 200

def test_about(client):
    """Test about page."""
    response = client.get('/about')
    assert response.status_code == 200

def test_contact(client):
    """Test contact page."""
    response = client.get('/contact')
    assert response.status_code == 200
