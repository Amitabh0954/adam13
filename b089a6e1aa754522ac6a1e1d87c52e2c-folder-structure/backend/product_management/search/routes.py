import logging
from flask import Blueprint, request, jsonify
from sqlalchemy import or_
from sqlalchemy.orm import load_only
from .models import db, Product

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

search_bp = Blueprint('search_bp', __name__)

RESULTS_PER_PAGE = 10

@search_bp.route('/products/search', methods=['GET'])
def search_products():
    query = request.args.get('query', '')
    page = int(request.args.get('page', 1))

    base_query = Product.query.filter(
        Product.is_deleted == False,
        or_(
            Product.name.ilike(f'%{query}%'),
            Product.category.ilike(f'%{query}%'),
            Product.attributes.ilike(f'%{query}%')
        )
    ).options(load_only('id', 'name', 'description', 'category', 'attributes')).paginate(page, RESULTS_PER_PAGE, False)

    products = base_query.items

    results = []
    for product in products:
        result = {
            'id': product.id,
            'name': highlight_terms(product.name, query),
            'description': highlight_terms(product.description, query),
            'category': product.category,
            'attributes': highlight_terms(product.attributes, query) if product.attributes else None
        }
        results.append(result)

    return jsonify({
        'total_results': base_query.total,
        'total_pages': base_query.pages,
        'current_page': page,
        'products': results
    }), 200

def highlight_terms(text: str, terms: str) -> str:
    for term in terms.split():
        text = text.replace(term, f'<b>{term}</b>')
    return text