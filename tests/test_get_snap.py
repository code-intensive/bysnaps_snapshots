from fastapi import FastAPI
from fastapi.testclient import TestClient
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND
from utils.id_generator import generate_uuid


def test_snap_exists(client: TestClient, fast_api_app: FastAPI) -> None:
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

    create_snap_endpoint = fast_api_app.url_path_for("create_snap")
    create_snap_response = client.post(create_snap_endpoint, json=data)
    assert create_snap_response.status_code == HTTP_201_CREATED

    created_snap = create_snap_response.json()

    get_snap_endpoint = fast_api_app.url_path_for(
        "get_snap",
        snap_id=created_snap["id"],
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
    get_snap_endpoint = fast_api_app.url_path_for("get_snap", snap_id=snap_uuid)

    response = client.get(get_snap_endpoint)

    assert response.status_code == HTTP_404_NOT_FOUND
    assert "id" not in response.json()
    assert response.json()["detail"][0]["msg"] == "snap not found"
