from typing import Any

from fastapi import FastAPI
from fastapi.testclient import TestClient
from starlette.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND


def test_snap_deletes(
    client: TestClient,
    fast_api_app: FastAPI,
    create_snap_fixture: Any,
) -> None:
    created_snap = create_snap_fixture()

    delete_snap_endpoint = fast_api_app.url_path_for(
        "delete_snap",
        id=created_snap["id"],
    )
    response = client.delete(delete_snap_endpoint)

    assert response.status_code == HTTP_204_NO_CONTENT
    assert response.content == b""

    get_snap_endpoint = fast_api_app.url_path_for(
        "get_snap",
        id=created_snap["id"],
    )
    response = client.get(get_snap_endpoint)

    assert response.status_code == HTTP_404_NOT_FOUND
    assert response.json()["detail"] == "snap not found"
