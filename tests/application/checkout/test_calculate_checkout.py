from src.application import CalculateCheckout
from src.domain import CartProduct, Cart
from src.infra.repositories import ProductRepository


class TestCalculateCheckout:
    def test_checkout(self):
        cart_product = CartProduct(id=1, quantity=10)
        cart = Cart(products=[cart_product])

        product_repository = ProductRepository()

        checkout_total = CalculateCheckout(cart, product_repository, [])

        checkout = checkout_total.calculate()

        assert checkout.total_amount == 10 * 15157
        assert checkout.total_discount == 0
        assert checkout.total_amount_with_discount == 10 * 15157
        assert checkout.products[0].id == 1
        assert checkout.products[0].quantity == 10
        assert checkout.products[0].total_amount == 10 * 15157
        assert checkout.products[0].is_gift is False
        assert checkout.products[0].discount == 0
