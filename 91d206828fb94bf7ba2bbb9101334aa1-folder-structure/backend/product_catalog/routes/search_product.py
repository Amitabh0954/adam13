# Epic Title: Product Catalog Management
from flask import Blueprint, request, jsonify
from services.product_service import ProductService

search_product_bp = Blueprint('search_product', __name__)
product_service = ProductService()

@search_product_bp.route('/search', methods=['GET'])
def search_products():
    query = request.args.get('query')
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    if not query:
        return jsonify({"error": "Search query is required"}), 400

    response = product_service.search_products(query, page, per_page)

    if response.get("error"):
        return jsonify(response), 400

    return jsonify(response), 200