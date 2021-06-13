from src.application import CalculateCheckoutTotals
from src.application.sales_rules import BlackFriday, ProductDiscount
from src.data.contracts import ProductRepositoryContract
from src.data.contracts.discount_repository_contract import DiscountRepositoryContract
from src.domain import Checkout, Cart
from src.application.checkout.contracts import CalculateCheckoutContract


class CalculateCheckout(CalculateCheckoutContract):
    def __init__(
        self,
        cart: Cart,
        product_repository: ProductRepositoryContract,
        discount_repository: DiscountRepositoryContract,
    ):
        self.__cart = cart
        self.__product_repository = product_repository
        self.__discount_repository = discount_repository

    def calculate(self) -> Checkout:
        checkout = CalculateCheckoutTotals(
            self.__cart, self.__product_repository
        ).calculate()
        self.__apply_sales_rules(checkout)
        return checkout

    def __apply_sales_rules(self, checkout: Checkout):
        BlackFriday(checkout, self.__product_repository)
        ProductDiscount(checkout, self.__discount_repository)
