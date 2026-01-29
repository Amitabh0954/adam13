# Epic Title: Product Catalog Management

from flask import Blueprint, request, jsonify
from structured_logging import get_logger
from backend.product_catalog_management.services.category_service import CategoryService
from backend.product_catalog_management.repositories.category_repository import CategoryRepository

category_blueprint = Blueprint('category_controller', __name__)
logger = get_logger(__name__)

@category_blueprint.route('/categories', methods=['POST'])
def add_category():
    data = request.json
    name = data.get('name')
    parent_id = data.get('parent_id', None)
    
    category_repository = CategoryRepository()  # Ideally should be injected
    category_service = CategoryService(category_repository)
    
    category = category_service.add_category(name, parent_id)
    if category is None:
        return jsonify({'message': 'Category addition failed'}), 400
    
    return jsonify({'message': 'Category added successfully', 'category_id': category.id})

@category_blueprint.route('/categories', methods=['GET'])
def list_all_categories():
    category_repository = CategoryRepository()  # Ideally should be injected
    category_service = CategoryService(category_repository)
    
    categories = category_service.list_all_categories()
    return jsonify(categories)