import falcon
from falcon import testing
import pytest
import ujson

from greetings.app import api


@pytest.fixture
def client():
    test_api = testing.TestClient(api)
    return test_api


# pytest will inject the object returned by the "client" function
# as an additional parameter.
def test_hello_world_get(client):
    response = client.simulate_get('/hello_world')
    assert response.status == falcon.HTTP_200
    assert "hello world" in response.json['message'].lower()
    assert "utc" in response.json['message'].lower()


def test_hello_world_invalid_post(client):
    response = client.simulate_post('/hello_world', body='<a>b</a>')
    assert response.status == falcon.HTTP_415


def test_hello_world_valid_post(client):
    test_payload = ujson.dumps({'fruit': 'apple', 'color': 'red'})
    response = client.simulate_post('/hello_world', body=test_payload)
    assert response.status == falcon.HTTP_201
    assert len(response.json['payloadKeys']) == 2
    assert set(response.json['payloadKeys']) == set(['fruit', 'color'])


def test_get_version(client):
    response = client.simulate_get('/version')
    assert response.status == falcon.HTTP_200
