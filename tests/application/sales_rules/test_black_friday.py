from datetime import datetime, timedelta

import pytest

from src.application.sales_rules import BlackFriday
from src.domain import Checkout, CheckoutProduct
from src.infra.repositories import ProductRepository


@pytest.fixture()
def checkout():
    checkout = Checkout(
        total_amount=100,
        total_discount=10,
        total_amount_with_discount=90,
        products=[
            CheckoutProduct(
                total_amount=100,
                is_gift=False,
                discount=10,
                quantity=1,
                unit_amount=100,
                id=1,
            )
        ],
    )
    yield checkout


@pytest.fixture()
def repository():
    product_repo = ProductRepository()
    yield product_repo


class TestBlackFriday:
    def test_append_gift(self, checkout, repository):
        black_friday = BlackFriday(
            checkout,
            repository,
            black_friday_date=datetime.now().today().strftime("%Y-%m-%d"),
        )
        black_friday.apply_sales_rule()

        assert len(checkout.products) == 2

    def test_today_is_not_black_friday(self, checkout, repository):
        black_friday = BlackFriday(
            checkout,
            repository,
            black_friday_date=(datetime.now() - timedelta(1)).strftime("%Y-%m-%d"),
        )
        black_friday.apply_sales_rule()

        assert len(checkout.products) == 1
