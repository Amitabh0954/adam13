from flask import Blueprint, request, jsonify
from backend.services.product.product_service import ProductService
import logging

logger = logging.getLogger(__name__)
product_bp = Blueprint('product', __name__)

product_service = ProductService()

@product_bp.route('/add', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    description = data.get('description')

    if not name or not description or price is None:
        logger.warning("Name, price, and description are required to add a product")
        return jsonify({"message": "Name, price, and description are required"}), 400

    try:
        product_service.add_product(name, price, description)
        logger.info(f"Product added with name: {name}")
        return jsonify({"message": "Product added successfully"}), 201
    except ValueError as e:
        logger.warning(f"Adding product failed: {str(e)}")
        return jsonify({"message": str(e)}), 400