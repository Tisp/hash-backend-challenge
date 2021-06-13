from src.application import CalculateCheckoutTotals
from src.application.sales_rules.constracts import SalesRulesContract
from src.data.contracts import ProductRepositoryContract
from src.domain import Checkout, Cart
from src.application.checkout.contracts import CalculateCheckoutContract
from typing import List


class CalculateCheckout(CalculateCheckoutContract):
    def __init__(
        self,
        cart: Cart,
        product_repository: ProductRepositoryContract,
        sales_rules: List[SalesRulesContract],
    ):
        self.__cart = cart
        self.__product_repository = product_repository
        self.__sales_rules = sales_rules

    def calculate(self) -> Checkout:
        checkout = CalculateCheckoutTotals(
            self.__cart, self.__product_repository
        ).calculate()
        for sale_rules in self.__sales_rules:
            sale_rules.apply_sales_rule(checkout)
        return checkout
