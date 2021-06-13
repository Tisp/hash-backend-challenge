import json
from flask import Blueprint, Response, request
from src.application import CalculateCheckout
from src.application.sales_rules import BlackFriday, ProductDiscount
from src.domain import Cart, CartProduct
from src.infra.repositories import (
    ProductRepository,
    DiscountRepository,
    ProductNotFound,
)
import dataclasses


blueprint = Blueprint("checkout", __name__)


@blueprint.route("/checkout", methods=["POST"])
def checkout():
    cart_json = request.get_json()
    cart = Cart([CartProduct(**p) for p in cart_json["products"]])
    product_repository = ProductRepository()
    discount_repository = DiscountRepository()

    sales_rules_list = [
        BlackFriday(product_repository),
        ProductDiscount(discount_repository),
    ]

    try:
        checkout = CalculateCheckout(cart, product_repository, sales_rules_list)
        result = checkout.calculate()
        body = dataclasses.asdict(result)
        status_code = 201
    except ProductNotFound as e:
        body = {"message": str(e)}
        status_code = 404

    return Response(
        json.dumps(body),
        mimetype="application/json",
        status=status_code,
    )
