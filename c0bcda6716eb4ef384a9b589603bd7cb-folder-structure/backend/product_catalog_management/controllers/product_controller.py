# Epic Title: Product Catalog Management

from flask import Blueprint, request, jsonify
from structured_logging import get_logger
from backend.product_catalog_management.services.product_service import ProductService
from backend.product_catalog_management.repositories.product_repository import ProductRepository

product_blueprint = Blueprint('product_controller', __name__)
logger = get_logger(__name__)

@product_blueprint.route('/products', methods=['POST'])
def add_product():
    data = request.json
    name = data.get('name')
    price = data.get('price')
    description = data.get('description')
    
    product_repository = ProductRepository()  # Ideally should be injected
    product_service = ProductService(product_repository)
    
    product = product_service.add_product(name, price, description)
    if product is None:
        return jsonify({'message': 'Product addition failed'}), 400
    
    return jsonify({'message': 'Product added successfully', 'product_id': product.id})

@product_blueprint.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id: int):
    data = request.json
    name = data.get('name')
    price = data.get('price')
    description = data.get('description')
    
    product_repository = ProductRepository()  # Ideally should be injected
    product_service = ProductService(product_repository)
    
    success = product_service.update_product(product_id, name, price, description)
    if not success:
        return jsonify({'message': 'Product update failed'}), 400
    
    return jsonify({'message': 'Product updated successfully'})