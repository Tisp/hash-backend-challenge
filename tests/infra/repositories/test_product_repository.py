from src.domain import Product
from src.infra.repositories import ProductRepository, ProductNotFound
import pytest


@pytest.fixture()
def repository():
    product_repo = ProductRepository()
    yield product_repo


class TestProductRepository:
    def test_get_product(self, repository):
        product = repository.get_product(1)
        assert type(product) == Product
        assert product.id == 1
        assert product.title == "Ergonomic Wooden Pants"
        assert product.amount == 15157
        assert product.is_gift is False
        assert product.description == "Deleniti beatae porro."

    def test_get_product_not_fount(self, repository):
        with pytest.raises(ProductNotFound):
            repository.get_product(1000000)
