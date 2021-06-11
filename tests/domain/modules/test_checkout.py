from src.domain import Checkout, Product


class TestProduct:
    def test_product_model_init(self):
        product = Product(
            amount=1200,
            description="Some Description",
            is_gift=False,
            title="Some title",
            id=12,
        )
        checkout = Checkout(
            total_amount=1000,
            total_discount=100,
            total_amount_with_discount=900,
            products=[product],
        )

        assert checkout.total_amount == 1000
        assert checkout.total_discount == 100
        assert checkout.total_amount_with_discount == 900
        assert checkout.products == [product]
