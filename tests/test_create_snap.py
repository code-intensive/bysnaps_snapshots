from fastapi import FastAPI
from fastapi.testclient import TestClient
from starlette.status import HTTP_200_OK, HTTP_201_CREATED
from utils.id_generator import generate_uuid


def test_create_snap(client: TestClient, fast_api_app: FastAPI) -> None:
    data = {
        "store_id": generate_uuid("store"),
        "customer_id": generate_uuid("customer"),
        "description": "A fake description for a fake snap purchase",
        "products": [
            {"product_id": generate_uuid("product"), "quantity": 10},
            {"product_id": generate_uuid("product"), "quantity": 14},
            {"product_id": generate_uuid("product"), "quantity": 31},
        ],
    }
    create_snap_endpoint = fast_api_app.url_path_for("get_snaps")
    response = client.post(create_snap_endpoint, json=data)

    assert response.status_code == HTTP_201_CREATED

    created_snap = response.json()
    assert "id" in created_snap
    assert data["store_id"] == created_snap["store_id"]
    assert len(data["products"]) == len(created_snap["products"])

    created_snap_url = fast_api_app.url_path_for("get_snap", snap_id=created_snap["id"])
    response = client.get(created_snap_url)

    assert response.status_code == HTTP_200_OK

    retrieved_snap = response.json()
    assert retrieved_snap["id"] == created_snap["id"]
    assert retrieved_snap["created_at"] == created_snap["created_at"]
    assert len(retrieved_snap["products"]) == len(created_snap["products"])
