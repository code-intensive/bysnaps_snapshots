from buysnaps_snapshots.main import app
from fastapi.testclient import TestClient
from starlette.status import HTTP_200_OK

client = TestClient(app)


def test_health_ok() -> None:
    url = app.url_path_for("health_check")
    response = client.request("get", url)
    assert response.status_code == HTTP_200_OK
    assert response.data is None
