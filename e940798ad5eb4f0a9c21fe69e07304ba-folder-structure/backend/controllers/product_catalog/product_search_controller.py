# Epic Title: Product Catalog Management
from flask import Blueprint, request, jsonify
from backend.services.product_catalog.product_search_service import ProductSearchService

product_search_bp = Blueprint('product_search', __name__)
product_search_service = ProductSearchService()

@product_search_bp.route('/api/product_catalog/search', methods=['GET'])
def search_products():
    query = request.args.get('query')
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', 10))
    
    if not query:
        return jsonify({"error": "Search query is required"}), 400

    response = product_search_service.search_products(query, page, page_size)
    return jsonify(response), 200