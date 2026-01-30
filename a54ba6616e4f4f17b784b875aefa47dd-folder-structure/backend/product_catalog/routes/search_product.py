# Epic Title: Product Catalog Management
from flask import Blueprint, request, jsonify
from services.product_service import ProductService

search_product_bp = Blueprint('search_product', __name__)
product_service = ProductService()

@search_product_bp.route('/search', methods=['GET'])
def search_products():
    search_term = request.args.get('q')
    page = request.args.get('page', 1, type=int)
    page_size = request.args.get('page_size', 10, type=int)
    
    results = product_service.search_products(search_term, page, page_size)
    
    return jsonify(results), 200