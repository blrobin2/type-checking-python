import json

import pytest

from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


def test_create_todo(client):
    response = client.post(
        "/todos",
        data=json.dumps(dict(
            title='Wash the dishes',
            done=False,
            deadline='2020-12-12'
        )),
        content_type='application/json'
    )

    assert response.status_code == 201


def test_create_todo_bad_request(client):
    response = client.post(
        "/todos",
        data=json.dumps(dict(
            title='Wash the dishes',
            done=False,
            deadline='WHENEVER'
        )),
        content_type='application/json'
    )

    assert response.status_code == 400
