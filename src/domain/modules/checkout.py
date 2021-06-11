from dataclasses import dataclass
from typing import List
from .product import Product


@dataclass(frozen=True)
class Checkout:
    total_amount: int
    total_amount_with_discount: int
    total_discount: int
    products: List[Product]
