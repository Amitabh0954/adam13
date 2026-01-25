import logging
from flask import Blueprint, request, jsonify, session
from sqlalchemy.orm import joinedload
from .models import db, Product, Category

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

catalog_bp = Blueprint('catalog_bp', __name__)

ADMIN_ROLE = 'admin'

def is_admin() -> bool:
    return session.get('role') == ADMIN_ROLE

@catalog_bp.route('/categories', methods=['POST'])
def add_category():
    if not is_admin():
        return jsonify({'message': 'Not authorized'}), 403

    data = request.get_json()
    name = data.get('name')
    parent_id = data.get('parent_id')

    if not name:
        return jsonify({'message': 'Category name is required'}), 400

    new_category = Category(name=name, parent_id=parent_id)
    db.session.add(new_category)
    db.session.commit()

    logger.info(f"Category {name} added successfully")
    return jsonify({'message': 'Category added successfully'}), 201

@catalog_bp.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    results = []

    def serialize(category):
        return {
            'id': category.id,
            'name': category.name,
            'parent_id': category.parent_id
        }

    for category in categories:
        results.append(serialize(category))

    return jsonify(results), 200

@catalog_bp.route('/products', methods=['POST'])
def add_product():
    if not is_admin():
        return jsonify({'message': 'Not authorized'}), 403

    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    category_id = data.get('category_id')

    if not name or not description or price is None or not category_id:
        return jsonify({'message': 'Name, description, price, and category are required'}), 400

    if price <= 0:
        return jsonify({'message': 'Price must be a positive number'}), 400

    if Product.query.filter_by(name=name).first() is not None:
        return jsonify({'message': 'Product name already exists'}), 400

    new_product = Product(name=name, description=description, price=price, category_id=category_id)
    db.session.add(new_product)
    db.session.commit()

    logger.info(f"Product {name} added successfully")
    return jsonify({'message': 'Product added successfully'}), 201

@catalog_bp.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id: int):
    if not is_admin():
        return jsonify({'message': 'Not authorized'}), 403

    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404

    data = request.get_json()
    description = data.get('description')
    price = data.get('price')
    category_id = data.get('category_id')

    if price is not None and price <= 0:
        return jsonify({'message': 'Price must be a positive number'}), 400

    if description:
        product.description = description
    if price is not None:
        product.price = price
    if category_id:
        product.category_id = category_id

    db.session.commit()

    logger.info(f"Product {product.name} updated successfully")
    return jsonify({'message': 'Product updated successfully'}), 200

@catalog_bp.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id: int):
    if not is_admin():
        return jsonify({'message': 'Not authorized'}), 403

    product = Product.query.get(product_id)
    if not product or product.is_deleted:
        return jsonify({'message': 'Product not found or already deleted'}), 404

    product.is_deleted = True
    db.session.commit()

    logger.info(f"Product {product.name} marked as deleted")
    return jsonify({'message': 'Product marked as deleted and will not appear in the catalog'}), 200

@catalog_bp.route('/products/search', methods=['GET'])
def search_products():
    query = request.args.get('query', '')
    page = int(request.args.get('page', 1))

    base_query = Product.query.filter(
        Product.is_deleted == False,
        or_(
            Product.name.ilike(f'%{query}%'),
            Product.category.has(Category.name.ilike(f'%{query}%')),
            Product.attributes.ilike(f'%{query}%')
        )
    ).options(joinedload(Product.category)).paginate(page, RESULTS_PER_PAGE, False)

    products = base_query.items

    results = []
    for product in products:
        result = {
            'id': product.id,
            'name': highlight_terms(product.name, query),
            'description': highlight_terms(product.description, query),
            'category': product.category.name,
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