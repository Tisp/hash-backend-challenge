from abc import ABC, abstractmethod
from src.data.contracts import ProductRepositoryContract
from src.domain import Cart, Checkout


class CalculateCheckoutTotalsContract(ABC):
    @abstractmethod
    def __init__(self, cart: Cart, product_repository: ProductRepositoryContract):
        raise Exception("Method not implemented")

    @abstractmethod
    def calculate(self) -> Checkout:
        raise Exception("Method not implemented")
