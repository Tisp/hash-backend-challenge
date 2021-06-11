from dataclasses import dataclass
from typing import List


@dataclass
class CheckoutProduct:
    id: int
    quantity: int
    unit_amount: int
    total_amount: int
    discount: int
    is_gift: bool


@dataclass(frozen=True)
class Checkout:
    total_amount: int
    total_amount_with_discount: int
    total_discount: int
    products: List[CheckoutProduct]
