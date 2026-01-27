from flask import request, jsonify
from flask_login import login_required, current_user
from . import product_blueprint
from .models import Product
from .extensions import db

@product_blueprint.route('/add_product', methods=['POST'])
@login_required
def add_product():
    # Ensure user is an admin
    if not current_user.is_admin:
        return jsonify({"error": "Only admins can add products"}), 403

    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    description = data.get('description')

    if Product.query.filter_by(name=name).first():
        return jsonify({"error": "Product name must be unique"}), 400

    if not isinstance(price, (int, float)) or price <= 0:
        return jsonify({"error": "Product price must be a positive number"}), 400

    if not description:
        return jsonify({"error": "Product description cannot be empty"}), 400

    new_product = Product(name=name, price=price, description=description)
    db.session.add(new_product)
    db.session.commit()

    return jsonify({"message": "Product added successfully"}), 201

@product_blueprint.route('/update_product/<int:product_id>', methods=['PUT'])
@login_required
def update_product(product_id):
    # Ensure user is an admin
    if not current_user.is_admin:
        return jsonify({"error": "Only admins can update products"}), 403

    data = request.get_json()
    product = Product.query.get_or_404(product_id)

    price = data.get('price')
    description = data.get('description', product.description)

    if 'price' in data:
        if not isinstance(price, (int, float)) or price <= 0:
            return jsonify({"error": "Product price must be a positive number"}), 400
        product.price = price

    if 'description' in data:
        if not description:
            return jsonify({"error": "Product description cannot be empty"}), 400
        product.description = data.get('description', product.description)

    db.session.commit()
    return jsonify({"message": "Product updated successfully"}), 200

@product_blueprint.route('/delete_product/<int:product_id>', methods=['DELETE'])
@login_required
def delete_product(product_id):
    # Ensure user is an admin
    if not current_user.is_admin:
        return jsonify({"error": "Only admins can delete products"}), 403

    data = request.get_json()
    confirm = data.get('confirm', False)
    
    if not confirm:
        return jsonify({"error": "Deletion requires confirmation"}), 400

    product = Product.query.get_or_404(product_id)
    
    db.session.delete(product)
    db.session.commit()

    return jsonify({"message": "Product deleted successfully"}), 200

@product_blueprint.route('/search_products', methods=['GET'])
def search_products():
    query = request.args.get('q', '')
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    products = Product.query.filter(
        Product.name.contains(query) | 
        Product.description.contains(query)
    ).paginate(page, per_page, False)

    results = []
    for product in products.items:
        result = {
            "id": product.id,
            "name": highlight_search_terms(product.name, query),
            "price": product.price,
            "description": highlight_search_terms(product.description, query)
        }
        results.append(result)

    return jsonify({
        "products": results,
        "total": products.total,
        "page": products.page,
        "pages": products.pages
    }), 200

def highlight_search_terms(text: str, terms: str) -> str:
    for term in terms.split():
        text = text.replace(term, f"<mark>{term}</mark>")
    return text