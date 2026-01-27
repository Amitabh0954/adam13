from flask import Blueprint, request, jsonify, session
from flask_login import login_required, current_user
from backend.repositories.shopping_cart.cart_repository import CartRepository
from backend.repositories.product_catalog.product_repository import ProductRepository

add_to_cart_controller = Blueprint('add_to_cart_controller', __name__)
cart_repository = CartRepository()
product_repository =