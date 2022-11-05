from fastapi.testclient import TestClient
from starlette.status import HTTP_200_OK


def test_health_ok(client: TestClient, api_endpoints: dict[str, str]) -> None:
    health_check_enpoint = api_endpoints["health_check"]
    response = client.request("get", health_check_enpoint)
    assert response.content == b"null"
    assert response.status_code == HTTP_200_OK
    assert response.url.endswith("/v1/snap-shots/health-check")
