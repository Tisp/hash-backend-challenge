from src.infra.repositories import DiscountRepository
import pytest


@pytest.fixture()
def repository():
    discount_repo = DiscountRepository()
    yield discount_repo


class TestProductRepository:
    def test_get_product(self, repository):
        discount = repository.get_discount(1)
        assert type(discount) == float
        assert 0 <= discount <= 0.5
