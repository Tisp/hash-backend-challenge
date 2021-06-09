from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    """Product Model"""

    id: int
    title: str
    description: str
    amount: int
    is_gift: bool

    def __str__(self):
        return f"{self.title} [{self.id}] | {self.description}"
