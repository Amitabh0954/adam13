from flask import request, jsonify
from flask_login import login_required, current_user
from sqlalchemy import or_
from . import product_blueprint, category_blueprint
from .models import Product, Category, CartItem
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
    category_ids = data.get('category_ids', [])

    if Product.query.filter_by(name=name).first():
        return jsonify({"error": "Product name must be unique"}), 400

    if not isinstance(price, (int, float)) or price <= 0:
        return jsonify({"error": "Product price must be a positive number"}), 400

    if not description:
        return jsonify({"error": "Product description cannot be empty"}), 400

    if not category_ids:
        return jsonify({"error": "At least one category must be selected"}), 400

    categories = Category.query.filter(Category.id.in_(category_ids)).all()
    if not categories:
        return jsonify({"error": "Invalid category IDs provided"}), 400

    new_product = Product(name=name, price=price, description=description, categories=categories)
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
    category_ids = data.get('category_ids', [category.id for category in product.categories])

    if 'price' in data:
        if not isinstance(price, (int, float)) or price <= 0:
            return jsonify({"error": "Product price must be a positive number"}), 400
        product.price = price

    if 'description' in data:
        if not description:
            return jsonify({"error": "Product description cannot be empty"}), 400
        product.description = description

    if 'category_ids' in data:
        if not category_ids:
            return jsonify({"error": "At least one category must be selected"}), 400
        categories = Category.query.filter(Category.id.in_(category_ids)).all()
        if not categories:
            return jsonify({"error": "Invalid category IDs provided"}), 400
        product.categories = categories

    db.session.commit()
    return jsonify({"message": "Product updated successfully"}), 200

@product_blueprint.route('/delete_product/<int:product_id>', methods=['DELETE'])
@login_required
def delete_product(product_id):
    # Ensure user is an admin
    if not current_user.is_admin:
        return jsonify({"error": "Only admins can delete products"}), 403

    data = request.get_json()
    confirmation = data.get('confirmation')
    if confirmation != "yes":
        return jsonify({"error": "Deletion requires confirmation"}), 400

    product = Product.query.get_or_404(product_id)
    product.is_active = False
    db.session.commit()
    return jsonify({"message": "Product deleted successfully"}), 200

@product_blueprint.route('/search_products', methods=['GET'])
def search_products():
    search_term = request.args.get('search_term', '')
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    products = Product.query.filter(
        Product.is_active,
        or_(
            Product.name.like(f'%{search_term}%'),
            Product.description.like(f'%{search_term}%'),
            Product.categories.any(Category.name.like(f'%{search_term}%'))
        )
    ).paginate(page, per_page, False)
    
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

@category_blueprint.route('/categories', methods=['POST'])
@login_required
def create_category():
    if not current_user.is_admin:
        return jsonify({"error": "Only admins can create categories"}), 403

    data = request.get_json()
    name = data.get('name')
    parent_id = data.get('parent_id')

    if name is None or name == "":
        return jsonify({"error": "Category name is required"}), 400

    if Category.query.filter_by(name=name).first():
        return jsonify({"error": "Category name must be unique"}), 400

    parent = None
    if parent_id:
        parent = Category.query.get(parent_id)
        if parent is None:
            return jsonify({"error": "Parent category not found"}), 404

    new_category = Category(name=name, parent=parent)
    db.session.add(new_category)
    db.session.commit()

    return jsonify({"message": "Category created successfully"}), 201

@category_blueprint.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    all_categories = [{
        "id": category.id,
        "name": category.name,
        "parent_id": category.parent_id
    } for category in categories]

    return jsonify({"categories": all_categories}), 200

@category_blueprint.route('/categories/<int:category_id>', methods=['PUT'])
@login_required
def update_category(category_id):
    if not current_user.is_admin:
        return jsonify({"error": "Only admins can update categories"}), 403
    
    data = request.get_json()
    name = data.get('name')
    parent_id = data.get('parent_id')

    category = Category.query.get_or_404(category_id)

    if name:
        if Category.query.filter_by(name=name).first():
            return jsonify({"error": "Category name must be unique"}), 400
        category.name = name

    if parent_id is not None:
        parent = Category.query.get(parent_id)
        if parent is None:
            return jsonify({"error": "Parent category not found"}), 404
        category.parent = parent

    db.session.commit()
    return jsonify({"message": "Category updated successfully"}), 200

@category_blueprint.route('/categories/<int:category_id>', methods=['DELETE'])
@login_required
def delete_category(category_id):
    if not current_user.is_admin:
        return jsonify({"error": "Only admins can delete categories"}), 403

    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()

    return jsonify({"message": "Category deleted successfully"}), 200