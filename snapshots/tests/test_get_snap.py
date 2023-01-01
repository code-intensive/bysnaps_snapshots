from typing import Any

from fastapi import FastAPI
from fastapi.testclient import TestClient
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND


def test_snap_exists(
    client: TestClient,
    fast_api_app: FastAPI,
    create_snap_fixture: Any,
) -> None:
    created_snap = create_snap_fixture()

    get_snap_endpoint = fast_api_app.url_path_for(
        "get_snap",
        id=created_snap["id"],
    )

    response = client.get(get_snap_endpoint)
    assert response.status_code == HTTP_200_OK

    snap = response.json()
    assert snap["id"] == created_snap["id"]
    assert (snap["store_id"], snap["customer_id"]) == (
        created_snap["store_id"],
        created_snap["customer_id"],
    )


def test_snap_does_not_exist(client: TestClient, fast_api_app: FastAPI) -> None:
    snap_uuid = "snap_3c7abe3fe7ac49359c33ca39c5b56c33"
    get_snap_endpoint = fast_api_app.url_path_for("get_snap", id=snap_uuid)

    response = client.get(get_snap_endpoint)

    assert response.status_code == HTTP_404_NOT_FOUND
    assert "id" not in response.json()
    assert response.json()["detail"] == "snap not found"
