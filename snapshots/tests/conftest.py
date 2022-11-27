from typing import Any, Callable, Generator

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from snapshots.main import get_app
from snapshots.utils.id_generator import generate_uuid


@pytest.fixture(scope="session")
def client() -> Generator[TestClient, None, None]:
    with TestClient(get_app()) as test_client:
        yield test_client


@pytest.fixture
def fast_api_app() -> FastAPI:
    return get_app()


@pytest.fixture
def snap_data() -> dict[str, Any]:
    return {
        "store_id": generate_uuid("store"),
        "customer_id": generate_uuid("customer"),
        "description": "A fake description for a fake snap purchase",
        "snap_items": [
            {"item_id": generate_uuid("snap_item"), "quantity": 10},
            {"item_id": generate_uuid("snap_item"), "quantity": 14},
            {"item_id": generate_uuid("snap_item"), "quantity": 31},
        ],
    }


@pytest.fixture
def update_data() -> dict[str, Any]:
    return {
        "description": "Updated description for a fake purchase and fake snap",
        "snap_items": [
            {"item_id": generate_uuid("snap_item"), "quantity": 34},
            {"item_id": generate_uuid("snap_item"), "quantity": 11},
        ],
    }


@pytest.fixture
def create_snap_fixture(
    fast_api_app: FastAPI,
    client: TestClient,
    snap_data: Callable[[], dict[str, Any]],
) -> Callable[[], dict[str, Any]]:
    create_snap_endpoint = fast_api_app.url_path_for("get_snaps")

    def _create_snap() -> dict[str, str | Any]:
        response = client.post(create_snap_endpoint, json=snap_data)
        return response.json()

    return _create_snap
