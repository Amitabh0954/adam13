from flask import Blueprint, request, jsonify
from sqlalchemy import or_
from backend.repositories.product_catalog.product_repository import ProductRepository

search_product_controller = Blueprint('search_product_controller', __name__)
product_repository = ProductRepository()

@search_product_controller.route('/search_products', methods=['GET'])
def search_products():
    search_term = request.args.get('search_term', '')
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    products = product_repository.search_products(search_term, page, per_page)
    
    result = []
    for product in products.items:
        product_info = {
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "description": product.description,
            "categories": [category.name for category in product.categories]
        }
        result.append(product_info)

    response = {
        "total": products.total,
        "pages": products.pages,
        "current_page": products.page,
        "products": result
    }

    return jsonify(response), 200