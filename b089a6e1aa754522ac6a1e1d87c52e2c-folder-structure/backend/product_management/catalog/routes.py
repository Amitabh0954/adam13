import logging
from flask import Blueprint, request, jsonify, session
from .models import db, Product

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

catalog_bp = Blueprint('catalog_bp', __name__)

ADMIN_ROLE = 'admin'

def is_admin() -> bool:
    return session.get('role') == ADMIN_ROLE

@catalog_bp.route('/products', methods=['POST'])
def add_product():
    if not is_admin():
        return jsonify({'message': 'Not authorized'}), 403

    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')

    if not name or not description or price is None:
        return jsonify({'message': 'Name, description, and price are required'}), 400

    if price <= 0:
        return jsonify({'message': 'Price must be a positive number'}), 400

    if Product.query.filter_by(name=name).first() is not None:
        return jsonify({'message': 'Product name already exists'}), 400

    new_product = Product(name=name, description=description, price=price)
    db.session.add(new_product)
    db.session.commit()

    logger.info(f"Product {name} added successfully")
    return jsonify({'message': 'Product added successfully'}), 201

@catalog_bp.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id: int):
    if not is_admin():
        return jsonify({'message': 'Not authorized'}), 403

    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404

    data = request.get_json()
    description = data.get('description')
    price = data.get('price')

    if price is not None and price <= 0:
        return jsonify({'message': 'Price must be a positive number'}), 400

    if description:
        product.description = description
    if price is not None:
        product.price = price

    db.session.commit()

    logger.info(f"Product {product.name} updated successfully")
    return jsonify({'message': 'Product updated successfully'}), 200