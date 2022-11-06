from fastapi import FastAPI
from fastapi.testclient import TestClient
from starlette.status import HTTP_200_OK


def test_get_snaps(client: TestClient, fast_api_app: FastAPI) -> None:
    get_snap_endpoint = fast_api_app.url_path_for("get_snaps")
    response = client.get(get_snap_endpoint)

    assert response.status_code == HTTP_200_OK
    assert isinstance(response.json(), list)
