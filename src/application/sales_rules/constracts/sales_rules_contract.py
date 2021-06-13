from abc import ABC, abstractmethod
from src.domain import Checkout


class SalesRulesContract(ABC):
    @abstractmethod
    def apply_sales_rule(self, checkout: Checkout):
        raise Exception("Method not implemented")
