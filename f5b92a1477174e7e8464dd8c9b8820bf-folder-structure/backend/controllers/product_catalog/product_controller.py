from flask import Blueprint, request, jsonify
from backend.services.product_catalog.product_service import ProductService
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
    category_id = data.get('category_id')

    if not name or not price or not description:
        logger.warning("Name, price, and description are required")
        return jsonify({"message": "Name, price, and description are required"}), 400

    try:
        product_service.add_product(name, price, description, category_id)
        logger.info(f"Product '{name}' added successfully")
        return jsonify({"message": "Product added successfully"}), 201
    except ValueError as e:
        logger.warning(f"Failed to add product: {str(e)}")
        return jsonify({"message": str(e)}), 400