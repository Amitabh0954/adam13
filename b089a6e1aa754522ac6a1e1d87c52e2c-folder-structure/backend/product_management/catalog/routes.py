import logging
from flask import Blueprint, request, jsonify
from .models import db, Product

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

catalog_bp = Blueprint('catalog_bp', __name__)

@catalog_bp.route('/products', methods=['POST'])
def add_product():
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