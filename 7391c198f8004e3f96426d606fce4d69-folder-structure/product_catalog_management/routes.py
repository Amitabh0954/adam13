from flask import request, jsonify
from flask_login import login_required, current_user
from . import product_blueprint
from .models import Product, Category
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