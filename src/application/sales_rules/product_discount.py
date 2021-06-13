from src.application.sales_rules.constracts import SalesRulesContract
from src.domain import Checkout
from src.infra.repositories import DiscountRepository


class ProductDiscount(SalesRulesContract):
    def __init__(self, checkout: Checkout, discount_repository: DiscountRepository):
        self.__checkout = checkout
        self.__discount_repository = discount_repository

    def apply_sales_rule(self):
        for product in self.__checkout.products:
            discount_percentage = self.__discount_repository.get_discount(product.id)
            product.discount = round(discount_percentage * product.total_amount)
            print(discount_percentage, product.discount)
            self.__checkout.total_discount += product.discount
            self.__checkout.total_amount_with_discount -= product.discount
