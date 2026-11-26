import pytest
from fastapi.testclient import TestClient


@pytest.mark.parametrize(
    "method, endpoint, expected_status_code",
    [
        ("GET", "/health", 200),
        ("POST", "/health", 405),
        ("PUT", "/health", 405),
        ("DELETE", "/health", 405),
        ("GET", "/nonexistent", 404),
        ("GET", "/docs", 200),
        ("GET", "/openapi.json", 200),
    ],
)
def test_endpoint_status_code(
    client: TestClient,
    method: str,
    endpoint: str,
    expected_status_code: int,
) -> None:
    response = client.request(method, endpoint)

    assert response.status_code == expected_status_code


def test_health_check(client: TestClient) -> None:
    response = client.get("/health")

    assert response.json() == {"status": "ok"}
    assert response.status_code == 200
