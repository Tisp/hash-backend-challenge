from src.application.checkout.contracts import CalculateCheckoutTotalsContract
from src.data.contracts import ProductRepositoryContract
from src.domain import Checkout, Cart, Product, CartProduct, CheckoutProduct


class CalculateCheckoutTotals(CalculateCheckoutTotalsContract):
    def __init__(self, cart: Cart, product_repository: ProductRepositoryContract):
        self.__cart = cart
        self.__product_repository = product_repository
        self.__total_amount = 0
        self.__total_discount = 0
        self.__checkout_products = []

    def calculate(self) -> Checkout:
        for cart_product in self.__cart.products:
            product_data = self.__product_repository.get_product(cart_product.id)
            self.__sum_total_amount(cart_product, product_data)
            self.__append_products(cart_product, product_data)

        return Checkout(
            total_amount=self.__total_amount,
            total_amount_with_discount=self.__total_discount,
            total_discount=0,
            products=self.__checkout_products,
        )

    def __sum_total_amount(self, cart_product: CartProduct, product: Product):
        amount = cart_product.quantity * product.amount
        self.__total_amount = self.__total_discount = amount

    def __append_products(self, cart_product: CartProduct, product: Product):
        checkout_product = CheckoutProduct(
            id=product.id,
            quantity=cart_product.quantity,
            unit_amount=product.amount,
            total_amount=cart_product.quantity * product.amount,
            discount=0,
            is_gift=product.is_gift,
        )

        self.__checkout_products.append(checkout_product)
