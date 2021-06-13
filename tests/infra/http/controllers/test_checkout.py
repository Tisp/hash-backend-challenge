import pytest
from unittest import mock
import json

from src.domain import Checkout
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


@mock.patch("src.infra.http.controllers.checkout.CalculateCheckout.calculate")
def test_get(mock_use_case, client):
    mock_use_case.return_value = Checkout(**checkout)
    print(mock_use_case)
    http_response = client.post(
        "/checkout", json={"products": [{"id": 1, "quantity": 3}]}
    )
    print(http_response)
    assert json.loads(http_response.data.decode("UTF-8")) == checkout
    mock_use_case.assert_called()
    assert http_response.status_code == 201
    assert http_response.mimetype == "application/json"
