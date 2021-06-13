import json
from typing import Union

from src.data.contracts import ProductRepositoryContract
from src.domain import Product
import pathlib


class ProductNotFound(Exception):
    pass


class ProductRepository(ProductRepositoryContract):
    def __init__(self):
        self.__products = {}
        for product in ProductRepository.__load_product_file():
            self.__products[product["id"]] = Product(**product)

    @classmethod
    def __load_product_file(cls):
        current_path = pathlib.Path(__file__).parent.absolute()
        with open(f"{current_path}/data/product.json", "r") as product_json:
            return json.loads(product_json.read())

    def get_product(self, product_id: int) -> Union[Product, None]:
        product = self.__products.get(product_id)
        if not product:
            raise ProductNotFound(f"Product {product_id} not found")
        return product

    def get_gift_product(self) -> Union[Product, None]:
        for product in self.__products.values():
            if product.is_gift:
                return product
        return None
