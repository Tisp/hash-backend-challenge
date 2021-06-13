from abc import ABC, abstractmethod
from src.domain import Checkout


class SalesRulesContract(ABC):
    @abstractmethod
    def __init__(self, checkout: Checkout):
        raise Exception("Method not implemented")

    @abstractmethod
    def apply_sales_rule(self):
        raise Exception("Method not implemented")
