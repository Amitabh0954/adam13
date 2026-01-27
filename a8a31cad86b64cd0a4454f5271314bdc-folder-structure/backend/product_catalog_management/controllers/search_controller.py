# Epic Title: Product Catalog Management

from flask import Blueprint, request, jsonify
from backend.product_catalog_management.services.search_service import SearchService

search_bp = Blueprint('search_bp', __name__)
search_service = SearchService()

@search_bp.route('/search', methods=['GET'])
def search_products():
    query = request.args.get('query')
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    if not query:
        return jsonify({'message': 'Search query is required'}), 400

    results = search_service.search_products(query, page, per_page)
    return jsonify(results), 200