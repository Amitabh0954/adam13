# Epic Title: Search Products

from flask import Blueprint, request, jsonify
from services.product_catalog.product_search_service import ProductSearchService
from validators.product_catalog.product_search_validator import ProductSearchValidator

product_search_controller = Blueprint('product_search_controller', __name__)

@product_search_controller.route('/products/search', methods=['GET'])
def search_products():
    params = request.args
    validator = ProductSearchValidator(params)
    if validator.is_valid():
        service = ProductSearchService()
        results = service.search_products(params)
        return jsonify(results), 200
    return jsonify(validator.errors), 400