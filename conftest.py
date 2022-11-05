import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture(scope="module", name="client")
def client() -> TestClient:
    return TestClient(app)


@pytest.fixture(scope="module", name="api_endpoints")
def api_endpoints() -> dict[str, str]:
    return {
        "health_check": app.url_path_for("health_check"),
    }
