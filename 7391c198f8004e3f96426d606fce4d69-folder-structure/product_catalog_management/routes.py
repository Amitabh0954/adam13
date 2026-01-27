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