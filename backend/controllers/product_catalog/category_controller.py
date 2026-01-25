from flask import Blueprint, request, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from backend.services.product_catalog.category_service import CategoryService
from backend.services.product_catalog.product_category_service import ProductCategoryService

engine = create_engine('mysql+pymysql://username:password@localhost:3306/databasename')
Session = sessionmaker(bind=engine)

category_controller = Blueprint('category_controller', __name__)

@category_controller.route('/categories', methods=['POST'])
def add_category():
    session_db = Session()
    category_service = CategoryService(session_db)

    try:
        data = request.json
        category = category_service.add_category(data)
        return jsonify({"message": "Category added successfully", "category": category.name}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@category_controller.route('/categories', methods=['GET'])
def get_all_categories():
    session_db = Session()
    category_service = CategoryService(session_db)
    categories = category_service.get_all_categories()
    return jsonify({"categories": [category.name for category in categories]}), 200

@category_controller.route('/product-categories', methods=['POST'])
def add_product_category():
    session_db = Session()
    product_category_service = ProductCategoryService(session_db)

    try:
        data = request.json
        product_category = product_category_service.add_product_category(data)
        return jsonify({"message": "Product-Category association added successfully"}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@category_controller.route('/product-categories/<int:product_id>', methods=['GET'])
def get_product_categories(product_id):
    session_db = Session()
    product_category_service = ProductCategoryService(session_db)
    product_categories = product_category_service.get_product_categories(product_id)
    categories_list = [{"product_id": pc.product_id, "category_id": pc.category_id} for pc in product_categories]
    return jsonify({"product_categories": categories_list}), 200

#### 6. Update routes to include endpoints for managing categories and associating products with categories