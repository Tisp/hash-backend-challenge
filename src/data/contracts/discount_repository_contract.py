from abc import ABC, abstractmethod


class DiscountRepositoryContract(ABC):
    @abstractmethod
    def get_discount(self, product_id: int) -> float:
        raise Exception("Method not implemented")
