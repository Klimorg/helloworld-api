import json

import jsonschema
import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_hello(client: TestClient) -> None:
    response = client.get("/hello/")
    assert response.status_code == 200

    response = response.json()

    with open("tests/jsons/hello.schema.json") as schema:
        response_schema = json.load(schema)
        jsonschema.validate(response, response_schema)
