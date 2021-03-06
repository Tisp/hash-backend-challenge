import grpc
from src.data.contracts.discount_repository_contract import DiscountRepositoryContract
from src.infra.grpc.discount import DiscountStub, GetDiscountRequest
from src.config import GRPC_SERVER


class DiscountRepository(DiscountRepositoryContract):
    def __init__(self):
        channel = grpc.insecure_channel(GRPC_SERVER)
        self.__client = DiscountStub(channel)

    def get_discount(self, product_id: int) -> float:
        discount_percentage = self.__client.GetDiscount(
            GetDiscountRequest(productID=product_id)
        )
        return float(discount_percentage.percentage)
