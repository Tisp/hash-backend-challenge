from abc import ABC, abstractmethod

from src.domain import Checkout


class CalculateCheckoutContract(ABC):
    @abstractmethod
    def calculate(self) -> Checkout:
        raise Exception("Method not implemented")
