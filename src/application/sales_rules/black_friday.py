from src.application.sales_rules.constracts import SalesRulesContract
from src.domain import Checkout, CheckoutProduct
from datetime import datetime
from src.config import BLACK_FRIDAY_DATE
from src.infra.repositories import ProductRepository


class BlackFriday(SalesRulesContract):
    def __init__(
        self,
        checkout: Checkout,
        product_repository: ProductRepository,
        black_friday_date=None,
    ):
        self.__checkout = checkout
        self.__product_repository = product_repository
        self.__black_friday_date = black_friday_date

    def apply_sales_rule(self):
        if self.__is_black_friday():
            gift_product = self.__product_repository.get_gift_product()
            print(gift_product)
            if gift_product is not None and not self.__is_checkout_has_gift():
                self.__checkout.products.append(
                    CheckoutProduct(
                        id=gift_product.id,
                        quantity=1,
                        unit_amount=gift_product.amount,
                        total_amount=0,
                        discount=gift_product.amount,
                        is_gift=True,
                    )
                )

    def __is_checkout_has_gift(self):
        for product in self.__checkout.products:
            if product.is_gift:
                return True
        return False

    def __is_black_friday(self) -> bool:
        today = datetime.now().today().strftime("%Y-%m-%d")
        black_friday = self.__black_friday_date or BLACK_FRIDAY_DATE
        return today == black_friday
