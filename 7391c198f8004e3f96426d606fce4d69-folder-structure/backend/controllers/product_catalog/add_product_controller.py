from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.repositories.product_catalog.product_repository import ProductRepository

add_product_controller = Blueprint('add_product_controller', __name__)
product_repository = ProductRepository()

@add_product_controller.route('/add_product', methods=['POST'])
@login_required
def add_product():
    # Ensure user is an admin
    if not current_user.is_admin:
        return jsonify({"error": "Only admins can add products"}), 403

    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    description = data.get('description')
    category_ids = data.get('category_ids', [])

    if product_repository.get_product_by_name(name):
        return jsonify({"error": "Product name must be unique"}), 400

    if not isinstance(price, (int, float)) or price <= 0:
        return jsonify({"error": "Product price must be a positive number"}), 400

    if not description:
        return jsonify({"error": "Product description cannot be empty"}), 400

    if not category_ids:
        return jsonify({"error": "At least one category must be selected"}), 400

    categories = product_repository.get_categories_by_ids(category_ids)
    if not categories:
        return jsonify({"error": "Invalid category IDs provided"}), 400

    new_product = product_repository.create_product(name, price, description, categories)
    return jsonify({"message": "Product added successfully"}), 201