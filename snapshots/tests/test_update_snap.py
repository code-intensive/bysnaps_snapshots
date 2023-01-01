import json
from typing import Any

from fastapi import FastAPI
from fastapi.testclient import TestClient
from starlette.status import HTTP_204_NO_CONTENT


def test_snap_updates(
    client: TestClient,
    fast_api_app: FastAPI,
    create_snap_fixture: Any,
    update_data: dict[str, Any],
) -> None:
    created_snap = create_snap_fixture()
    update_data.update({"id": created_snap["id"]})
    update_snap_endpoint = fast_api_app.url_path_for(
        "update_snap",
        id=created_snap["id"],
    )
    response = client.patch(update_snap_endpoint, data=json.dumps(update_data))

    assert response.status_code == HTTP_204_NO_CONTENT
    assert response.content == b""

    get_snap_endpoint = fast_api_app.url_path_for(
        "get_snap",
        id=created_snap["id"],
    )
    response = client.get(get_snap_endpoint)

    updated_snap = response.json()
    assert updated_snap["id"] == created_snap["id"]
    assert updated_snap["last_modified"] is not None
    assert updated_snap["store_id"] == created_snap["store_id"]
    assert updated_snap["created_at"] == created_snap["created_at"]
    assert updated_snap["customer_id"] == created_snap["customer_id"]
    assert created_snap["description"] != updated_snap["description"]
    assert len(created_snap["snap_items"]) != len(updated_snap["snap_items"])
    assert (
        created_snap["snap_items"][0]["item_id"]
        != updated_snap["snap_items"][0]["item_id"]
    )
