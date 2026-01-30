# Epic Title: Product Catalog Management
from flask import Flask, request, jsonify
from backend.services.product_catalog_management.add_product_service import AddProductService
from backend.services.product_catalog_management.update_product_service import UpdateProductService
from backend.services.product_catalog_management.delete_product_service import DeleteProductService
from backend.services.product_catalog_management.search_product_service import SearchProductService
from backend.services.product_catalog_management.category_management_service import CategoryManagementService

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'

add_product_service = AddProductService()
update_product_service = UpdateProductService()
delete_product_service = DeleteProductService()
search_product_service = SearchProductService()
category_management_service = CategoryManagementService()

@app.route('/api/product_catalog_management/add_product', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    category_id = data.get('category_id')

    if not name or not description or price is None or category_id is None:
        return jsonify({"error": "Name, description, price, and category_id are required"}), 400
    
    response = add_product_service.add_product(name, description, price, category_id)

    if response.get("error"):
        return jsonify(response), 400

    return jsonify(response), 200

@app.route('/api/product_catalog_management/update_product/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    response = update_product_service.update_product(product_id, data)

    if response.get("error"):
        return jsonify(response), 400

    return jsonify(response), 200

@app.route('/api/product_catalog_management/delete_product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    response = delete_product_service.delete_product(product_id)

    if response.get("error"):
        return jsonify(response), 400

    return jsonify(response), 200

@app.route('/api/product_catalog_management/search_products', methods=['GET'])
def search_products():
    query = request.args.get('query')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    response = search_product_service.search_products(query, page, per_page)
    return jsonify(response), 200

@app.route('/api/product_catalog_management/categories', methods=['GET'])
def get_categories():
    response = category_management_service.get_all_categories()
    return jsonify(response), 200

@app.route('/api/product_catalog_management/category', methods=['POST'])
def create_category():
    data = request.get_json()
    name = data.get('name')
    parent_id = data.get('parent_id')

    if not name:
        return jsonify({"error": "Category name is required"}), 400

    response = category_management_service.create_category(name, parent_id)
    return jsonify(response), 200

@app.route('/api/product_catalog_management/category/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    data = request.get_json()
    name = data.get('name')
    parent_id = data.get('parent_id')

    if not name:
        return jsonify({"error": "Category name is required"}), 400

    response = category_management_service.update_category(category_id, name, parent_id)
    if response.get("error"):
        return jsonify(response), 400

    return jsonify(response), 200

@app.route('/api/product_catalog_management/category/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    response = category_management_service.delete_category(category_id)
    if response.get("error"):
        return jsonify(response), 400

    return jsonify(response), 200

@app.route('/')
def index():
    return "Welcome to the Product Catalog Management System"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)