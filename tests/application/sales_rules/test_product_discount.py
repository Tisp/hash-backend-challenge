import pytest

from src.application.sales_rules import ProductDiscount
from src.domain import Checkout, CheckoutProduct


@pytest.fixture()
def checkout():
    checkout = Checkout(
        total_amount=1000,
        total_discount=0,
        total_amount_with_discount=1000,
        products=[
            CheckoutProduct(
                total_amount=1000,
                is_gift=False,
                discount=0,
                quantity=1,
                unit_amount=1000,
                id=1,
            )
        ],
    )
    yield checkout


@pytest.fixture()
def repository():
    class Discount:
        def get_discount(self, id):
            return 0.05000000074505806

    yield Discount()


@pytest.fixture()
def repository_without_discount():
    class Discount:
        def get_discount(self, id):
            return 0.0

    yield Discount()


class TestProductDiscount:
    def test_apply_discount(self, checkout, repository):
        product_discount = ProductDiscount(
            checkout,
            repository,
        )

        product_discount.apply_sales_rule()

        assert checkout.total_amount == 1000
        assert checkout.total_discount == 50
        assert checkout.total_amount_with_discount == 950
        assert checkout.products[0].discount == 50

    def test_without_discount(self, checkout, repository_without_discount):
        product_discount = ProductDiscount(
            checkout,
            repository_without_discount,
        )

        product_discount.apply_sales_rule()

        assert checkout.total_amount == 1000
        assert checkout.total_discount == 0
        assert checkout.total_amount_with_discount == 1000
        assert checkout.products[0].discount == 0
