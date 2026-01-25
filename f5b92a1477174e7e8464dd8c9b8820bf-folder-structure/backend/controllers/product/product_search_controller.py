from flask import Blueprint, request, jsonify
from backend.services.product.product_search_service import ProductSearchService
import logging

logger = logging.getLogger(__name__)
product_search_bp = Blueprint('product_search', __name__)

product_search_service = ProductSearchService()

@product_search_bp.route('/products/search', methods=['GET'])
def search_products():
    query = request.args.get('query')
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    if not query:
        logger.warning("Search query is required")
        return jsonify({"message": "Search query is required"}), 400

    try:
        results = product_search_service.search_products(query, page, per_page)
        logger.info(f"Search results returned for query: {query}")
        return jsonify(results), 200
    except ValueError as e:
        logger.warning(f"Search failed: {str(e)}")
        return jsonify({"message": str(e)}), 400