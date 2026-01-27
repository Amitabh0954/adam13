# Epic Title: Product Catalog Management

from flask import Blueprint, request, jsonify
from backend.services.product_catalog.product_search_service import ProductSearchService

product_search_bp = Blueprint('product_search_bp', __name__)

@product_search_bp.route('/products/search', methods=['GET'])
def search_products():
    query = request.args.get('query')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    if not query:
        return jsonify({'message': 'Search query is required'}), 400

    product_search_service = ProductSearchService()
    results = product_search_service.search_products(query, page, per_page)

    return jsonify(results), 200