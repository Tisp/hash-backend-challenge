from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class CartProduct:
    id: int
    quantity: int


@dataclass(frozen=True)
class Cart:
    products: List[CartProduct]
