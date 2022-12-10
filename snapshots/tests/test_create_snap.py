import json
from typing import Any

from fastapi import FastAPI
from fastapi.testclient import TestClient
from starlette.status import HTTP_201_CREATED


def test_create_snap(
    client: TestClient,
    fast_api_app: FastAPI,
    snap_data: dict[str, Any],
) -> None:
    create_snap_endpoint = fast_api_app.url_path_for("create_snap")
    response = client.post(create_snap_endpoint, data=json.dumps(snap_data))

    assert response.status_code == HTTP_201_CREATED

    created_snap = response.json()
    assert "id" in created_snap
    assert snap_data["store_id"] == created_snap["store_id"]
    assert snap_data["customer_id"] == created_snap["customer_id"]
    assert snap_data["description"] == created_snap["description"]
    assert len(snap_data["snap_items"]) == len(created_snap["snap_items"])
