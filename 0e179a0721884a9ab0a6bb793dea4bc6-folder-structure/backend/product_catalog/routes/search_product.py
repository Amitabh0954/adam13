# Epic Title: Product Catalog Management
from flask import Blueprint, request, jsonify
from services.product_search_service import ProductSearchService

search_product_bp = Blueprint('search_product', __name__)
product_search_service = ProductSearchService()

@search_product_bp.route('/search', methods=['GET'])
def search_product():
    query = request.args.get('query')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    if not query:
        return jsonify({"error": "Search query is required"}), 400

    results = product_search_service.search_products(query, page, per_page)
    return jsonify(results), 200