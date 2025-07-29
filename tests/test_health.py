import pytest

def test_health_check(client):
    """Test the basic health check endpoint."""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert 'message' in data

def test_detailed_health_check(client):
    """Test the detailed health check endpoint."""
    response = client.get('/health/detailed')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert 'version' in data
    assert 'timestamp' in data