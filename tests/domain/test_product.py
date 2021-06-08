from src.domain import Product


class TestProduct:
    def test_product_model_init(self):
        product = Product(
            id=1,
            title="Some Product",
            description="Some product description",
            amount=1200,
            is_gift=False,
        )

        assert product.id == 1
        assert product.title == "Some Product"
        assert product.description == "Some product description"
        assert product.amount == 1200
        assert product.is_gift is False
