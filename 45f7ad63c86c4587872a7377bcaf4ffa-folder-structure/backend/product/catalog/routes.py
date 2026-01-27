# Epic Title: Product Catalog Management

from flask import Blueprint, request, jsonify
from models import Product  # Assuming models.py contains a Product model
from database import db_session

catalog_bp = Blueprint('catalog_bp', __name__)

@catalog_bp.route('/product', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    description = data.get('description')

    # Validate product name is unique
    if Product.query.filter_by(name=name).first():
        return jsonify({'message': 'Product name already exists'}), 400

    # Validate product price is positive
    if price <= 0:
        return jsonify({'message': 'Product price must be a positive number'}), 400

    # Validate product description is not empty
    if not description:
        return jsonify({'message': 'Product description cannot be empty'}), 400

    new_product = Product(name=name, price=price, description=description)
    db_session.add(new_product)
    db_session.commit()

    return jsonify({'message': 'Product added successfully'}), 201

@catalog_bp.route('/product/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()
    price = data.get('price')
    description = data.get('description')

    product = Product.query.get(id)

    if not product:
        return jsonify({'message': 'Product not found'}), 404

    # Validate product price is numeric and positive
    if not isinstance(price, (int, float)) or price <= 0:
        return jsonify({'message': 'Product price must be a positive number'}), 400

    # Description can be modified but not removed
    if description is None:
        return jsonify({'message': 'Product description cannot be removed'}), 400

    product.price = price
    product.description = description
    db_session.commit()

    return jsonify({'message': 'Product updated successfully'}), 200

@catalog_bp.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)

    if not product:
        return jsonify({'message': 'Product not found'}), 404

    # Assuming there is a confirmation step on frontend
    db_session.delete(product)
    db_session.commit()

    return jsonify({'message': 'Product deleted successfully'}), 200