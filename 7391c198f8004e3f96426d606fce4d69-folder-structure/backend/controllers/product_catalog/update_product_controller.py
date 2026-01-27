from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.repositories.product_catalog.product_repository import ProductRepository

update_product_controller = Blueprint('update_product_controller', __name__)
product_repository = ProductRepository()

@update_product_controller.route('/update_product/<int:product_id>', methods=['PUT'])
@login_required
def update_product(product_id):
    # Ensure user is an admin
    if not current_user.is_admin:
        return jsonify({"error": "Only admins can update products"}), 403

    data = request.get_json()
    product = product_repository.get_product_by_id(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    price = data.get('price')
    description = data.get('description', product.description)
    category_ids = data.get('category_ids', [category.id for category in product.categories])

    if 'price' in data:
        if not isinstance(price, (int, float)) or price <= 0:
            return jsonify({"error": "Product price must be a positive number"}), 400
        product.price = price

    if 'description' in data:
        if not description:
            return jsonify({"error": "Product description cannot be empty"}), 400
        product.description = description

    if 'category_ids' in data:
        if not category_ids:
            return jsonify({"error": "At least one category must be selected"}), 400
        categories = product_repository.get_categories_by_ids(category_ids)
        if not categories:
            return jsonify({"error": "Invalid category IDs provided"}), 400
        product.categories = categories

    product_repository.update_product(product)
    return jsonify({"message": "Product updated successfully"}), 200