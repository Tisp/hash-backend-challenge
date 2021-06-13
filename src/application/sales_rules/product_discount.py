from src.application.sales_rules.constracts import SalesRulesContract
from src.data.contracts.discount_repository_contract import DiscountRepositoryContract
from src.domain import Checkout


class ProductDiscount(SalesRulesContract):
    def __init__(
        self, checkout: Checkout, discount_repository: DiscountRepositoryContract
    ):
        self.__checkout = checkout
        self.__discount_repository = discount_repository

    def apply_sales_rule(self):
        for product in self.__checkout.products:
            discount_percentage = self.__discount_repository.get_discount(product.id)
            product.discount = round(discount_percentage * product.total_amount)
            print(discount_percentage, product.discount)
            self.__checkout.total_discount += product.discount
            self.__checkout.total_amount_with_discount -= product.discount