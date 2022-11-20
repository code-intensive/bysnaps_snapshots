from typing import Generator

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from main import app


@pytest.fixture(scope="session")
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def fast_api_app() -> FastAPI:
    return app
