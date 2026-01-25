from flask import Blueprint, request, jsonify
from backend.services.product_catalog.product_search_service import ProductSearchService
import logging

logger = logging.getLogger(__name__)
product_search_bp = Blueprint('product_search', __name__)

product_search_service = ProductSearchService()

@product_search_bp.route('/products/search', methods=['GET'])
def search_products():
    query = request.args.get('query', '')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    if not query:
        logger.warning("Search query is required")
        return jsonify({"message": "Search query is required"}), 400
    
    results, total = product_search_service.search_products(query, page, per_page)
    return jsonify({
        "results": results,
        "total": total,
        "page": page,
        "per_page": per_page
    }), 200