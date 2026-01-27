# Epic Title: Product Catalog Management

from flask import Blueprint, request, jsonify
from sqlalchemy import or_
from models import Product

search_bp = Blueprint('search_bp', __name__)

@search_bp.route('/search', methods=['GET'])
def search_products():
    search_term = request.args.get('q', '')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    
    if not search_term:
        return jsonify({'message': 'Search term cannot be empty'}), 400
    
    search_query = f"%{search_term}%"
    products = Product.query.filter(
        or_(
            Product.name.ilike(search_query),
            Product.category.ilike(search_query),  # Assuming Product model has category field
            Product.attributes.ilike(search_query),  # Assuming Product model has attributes field
        )
    ).paginate(page, per_page, False)

    result = {
        'total': products.total,
        'pages': products.pages,
        'current_page': products.page,
        'next_num': products.next_num,
        'prev_num': products.prev_num,
        'has_next': products.has_next,
        'has_prev': products.has_prev,
        'items': [
            {
                'id': product.id,
                'name': product.name,
                'category': product.category,
                'attributes': product.attributes,
                'price': product.price,
                'description': product.description,
            } for product in products.items
        ]
    }

    return jsonify(result), 200