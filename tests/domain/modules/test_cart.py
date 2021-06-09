from src.domain import Cart, Product


class TestProduct:
    def test_product_model_init(self):
        product = Product(
            amount=1200,
            description="Some Description",
            is_gift=False,
            title="Some title",
            id=12,
        )
        cart = Cart(
            total_amount=1000,
            total_discount=100,
            total_amount_with_discount=900,
            products=[product],
        )

        assert cart.total_amount == 1000
        assert cart.total_discount == 100
        assert cart.total_amount_with_discount == 900
        assert cart.products == [product]
