from src.domain import Cart, CartProduct


class TestCart:
    def test_cart_model_init(self):
        cart_product = CartProduct(id=1, quantity=10)
        cart = Cart(products=[cart_product])

        assert cart.products[0].id == 1
        assert cart.products[0].quantity == 10
