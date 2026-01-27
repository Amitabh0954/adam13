from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.products.models.product import Product
from backend.products.repositories.product_repository import ProductRepository

product_blueprint = Blueprint('product', __name__)
product_repository = ProductRepository()

@product_blueprint.route('/add_product', methods=['POST'])
@login_required
def add_product():
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

@product_blueprint.route('/update_product/<int:product_id>', methods=['PUT'])
@login_required
def update_product(product_id):
    if not current_user.is_admin:
        return jsonify({"error": "Only admins can update products"}), 403

    data = request.get_json()
    price = data.get('price')
    description = data.get('description')

    product = product_repository.get_product_by_id(product_id)
    
    if not product:
        return jsonify({"error": "Product not found"}), 404

    if price is not None:
        if not isinstance(price, (int, float)) or price <= 0:
            return jsonify({"error": "Product price must be a positive number"}), 400
        product.price = price

    if description:
        product.description = description
    else:
        return jsonify({"error": "Product description cannot be emptied"}), 400

    updated_product = product_repository.update_product(product)
    return jsonify({"message": "Product updated successfully", "product": updated_product.to_dict()}), 200