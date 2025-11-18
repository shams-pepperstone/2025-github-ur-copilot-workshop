"""
Basic tests for Phase 1: Flask app foundation
Tests that the root route serves the index.html template
"""
import pytest
from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index_route_exists(client):
    """Test that the root route exists and returns 200"""
    response = client.get('/')
    assert response.status_code == 200


def test_index_route_returns_html(client):
    """Test that the root route returns HTML content"""
    response = client.get('/')
    assert response.content_type == 'text/html; charset=utf-8'


def test_index_route_contains_placeholder(client):
    """Test that the index page contains the placeholder text"""
    response = client.get('/')
    assert b'Pomodoro Timer App' in response.data


def test_static_files_configured(client):
    """Test that static files can be accessed"""
    # Test CSS file is accessible
    response = client.get('/static/style.css')
    assert response.status_code == 200
    
    # Test JS file is accessible
    response = client.get('/static/timer.js')
    assert response.status_code == 200