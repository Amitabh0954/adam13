# Epic Title: Product Catalog Management
from flask import Blueprint, request, jsonify
from services.search_product_service import SearchProductService

search_product_bp = Blueprint('search_product', __name__)

@search_product_bp.route('/search', methods=['GET'])
def search_product():
    query = request.args.get('query', '')
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', 10))
    
    product_service = SearchProductService()
    response = product_service.search_products(query, page, page_size)
    
    return jsonify(response), 200