from fastapi import FastAPI
from fastapi.testclient import TestClient
from starlette.status import HTTP_200_OK


def test_health_ok(client: TestClient, fast_api_app: FastAPI) -> None:
    health_check_endpoint = fast_api_app.url_path_for("health_check")
    response = client.request("get", health_check_endpoint)

    assert response.content == b"null"
    assert response.status_code == HTTP_200_OK
    assert response.url.endswith("/v1/snap-shots/health-check")
