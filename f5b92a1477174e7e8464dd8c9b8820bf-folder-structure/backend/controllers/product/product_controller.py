from flask import Blueprint, request, jsonify
from backend.services.product.product_service import ProductService
import logging

logger = logging.getLogger(__name__)
product_bp = Blueprint('product', __name__)

product_service = ProductService()

@product_bp.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    description = data.get('description')

    if not name or not description:
        logger.warning("Name and description are required to add a product")
        return jsonify({"message": "Name and description are required"}), 400
    
    if not isinstance(price, (int, float)) or price <= 0:
        logger.warning("Price must be a positive number")
        return jsonify({"message": "Price must be a positive number"}), 400

    try:
        product_service.add_product(name, price, description)
        logger.info(f"Product '{name}' added successfully")
        return jsonify({"message": "Product added successfully"}), 201
    except ValueError as e:
        logger.warning(f"Adding product failed: {str(e)}")
        return jsonify({"message": str(e)}), 400