# Epic Title: Product Catalog Management

from flask import Blueprint, request, jsonify
from models import Product, Category  # Assuming models.py contains Category model
from database import db_session

categorization_bp = Blueprint('categorization_bp', __name__)

@categorization_bp.route('/category', methods=['POST'])
def add_category():
    data = request.get_json()
    name = data.get('name')
    parent_id = data.get('parent_id', None)

    if Category.query.filter_by(name=name).first():
        return jsonify({'message': 'Category name already exists'}), 400

    new_category = Category(name=name, parent_id=parent_id)
    db_session.add(new_category)
    db_session.commit()

    return jsonify({'message': 'Category added successfully'}), 201

@categorization_bp.route('/product/<int:product_id>/category', methods=['POST'])
def categorize_product(product_id):
    data = request.get_json()
    category_id = data.get('category_id')

    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404

    category = Category.query.get(category_id)
    if not category:
        return jsonify({'message': 'Category not found'}), 404

    product.category_id = category_id  # Assuming Product model has category_id field
    db_session.commit()

    return jsonify({'message': 'Product categorized successfully'}), 200