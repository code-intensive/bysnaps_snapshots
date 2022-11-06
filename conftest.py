import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


@pytest.fixture
def fast_api_app() -> FastAPI:
    return app
