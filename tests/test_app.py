import falcon
from falcon import testing
import pytest

from greetings.app import api


@pytest.fixture
def client():
    test_api = testing.TestClient(api)
    return test_api


def test_hello_world(client):
    response = client.simulate_get('/hello_world')
    assert response.status == falcon.HTTP_200
    assert "hello world" in response.json['message'].lower()
    assert "utc" in response.json['message'].lower()