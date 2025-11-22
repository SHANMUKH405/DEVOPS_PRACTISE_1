"""
Unit tests for the Flask application
"""
import pytest
import json
from app import app

@pytest.fixture
def client():
    """Create a test client for the Flask application"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test the home page returns 200 status"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'DevOps Practice Project 1' in response.data

def test_health_endpoint(client):
    """Test the health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['status'] == 'healthy'
    assert 'timestamp' in data
    assert 'hostname' in data

def test_api_info_endpoint(client):
    """Test the API info endpoint"""
    response = client.get('/api/info')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['application'] == 'DevOps Practice Project 1'
    assert 'version' in data
    assert 'environment' in data
    assert 'hostname' in data
    assert 'timestamp' in data

def test_invalid_route(client):
    """Test that invalid routes return 404"""
    response = client.get('/invalid')
    assert response.status_code == 404
