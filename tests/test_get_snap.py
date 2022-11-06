from fastapi import FastAPI
from fastapi.testclient import TestClient
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND


def test_snap_exists(client: TestClient, fast_api_app: FastAPI) -> None:
    snap_uuid = "snap_3c7abe3fe7ac49359c33ca39c5b56c8f"
    get_snap_endpoint = fast_api_app.url_path_for("get_snap", snap_id=snap_uuid)

    response = client.get(get_snap_endpoint)

    assert response.status_code == HTTP_200_OK
    assert response.json()["id"] == snap_uuid


def test_snap_does_not_exist(client: TestClient, fast_api_app: FastAPI) -> None:
    snap_uuid = "snap_3c7abe3fe7ac49359c33ca39c5b56c33"
    get_snap_endpoint = fast_api_app.url_path_for("get_snap", snap_id=snap_uuid)

    response = client.get(get_snap_endpoint)

    assert response.status_code == HTTP_404_NOT_FOUND
    assert "id" not in response.json()
    assert response.json()["detail"] == "Snapshot not found"
