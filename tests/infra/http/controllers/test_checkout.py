import pytest
from unittest import mock
import json

from src.infra.http.app import create_app


@pytest.fixture
def app():
    app = create_app("testing")
    return app


checkout = {
    "total_amount": 45471,
    "total_amount_with_discount": 45471,
    "total_discount": 0,
    "products": [
        {
            "id": 1,
            "quantity": 3,
            "unit_amount": 15157,
            "total_amount": 45471,
            "discount": 0,
            "is_gift": False,
        }
    ],
}


@mock.patch("src.infra.http.controllers.checkout.checkout")
def test_get(mock_use_case, client):
    mock_use_case.return_value = checkout

    http_response = client.post(
        "/checkout", json={"products": [{"id": 1, "quantity": 3}]}
    )

    assert json.loads(http_response.data.decode("UTF-8")) == checkout
    assert http_response.status_code == 201
    assert http_response.mimetype == "application/json"
