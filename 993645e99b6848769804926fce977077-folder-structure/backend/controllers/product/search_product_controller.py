from flask import Blueprint, request, jsonify
from backend.services.product.search_product_service import SearchProductService
import logging

logger = logging.getLogger(__name__)
product_bp = Blueprint('product', __name__)

search_product_service = SearchProductService()

@product_bp.route('/search', methods=['GET'])
def search_products():
    query = request.args.get('q', '')
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    if not query:
        logger.warning("Search query is required")
        return jsonify({"message": "Search query is required"}), 400

    results = search_product_service.search_products(query, page, per_page)
    logger.info(f"Search conducted with query: {query}")
    return jsonify(results), 200