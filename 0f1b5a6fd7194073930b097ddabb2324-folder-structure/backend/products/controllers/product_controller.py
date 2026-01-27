from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.products.models.product import Product
from backend.products.repositories.product_repository import ProductRepository

product_blueprint = Blueprint('product', __name__)
product_repository = ProductRepository()

@product_blueprint.route('/add_product', methods=['POST'])
@login_required
def add_product():
    # Ensure user is an admin
    if not current_user.is_admin:
        return jsonify({"error": "Only admins can add products"}), 403

    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    description = data.get('description')

    if product_repository.get_product_by_name(name):
        return jsonify({"error": "Product name must be unique"}), 400

    if not isinstance(price, (int, float)) or price <= 0:
        return jsonify({"error": "Product price must be a positive number"}), 400

    if not description:
        return jsonify({"error": "Product description cannot be empty"}), 400

    new_product = product_repository.create_product(name, price, description)
    return jsonify({"message": "Product added successfully", "product": new_product.to_dict()}), 201