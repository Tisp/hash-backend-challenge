from abc import ABC, abstractmethod
from src.domain import Product
from typing import Union


class ProductRepositoryContract(ABC):
    @abstractmethod
    def get_product(self, id: int) -> Union[Product, None]:
        raise Exception("Method not implemented")

    @abstractmethod
    def get_gift_product(self) -> Union[Product, None]:
        raise Exception("Method not implemented")
