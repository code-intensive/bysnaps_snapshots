from typing import Any

from fastapi import FastAPI
from fastapi.testclient import TestClient
from starlette.status import HTTP_200_OK


def test_get_snaps(
    client: TestClient,
    fast_api_app: FastAPI,
    create_snap_fixture: Any,
) -> None:
    create_snap_fixture()
    create_snap_fixture()
    create_snap_fixture()
    get_snap_endpoint = fast_api_app.url_path_for("get_snaps")
    response = client.get(get_snap_endpoint)

    assert response.status_code == HTTP_200_OK
    retrieved_snaps = response.json()
    assert isinstance(retrieved_snaps, list)
    assert len(retrieved_snaps) >= 3
