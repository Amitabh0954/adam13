# Epic Title: Product Catalog Management

from flask import Flask, request, jsonify
import mysql.connector
from backend.repositories.product_catalog.product_repository import ProductRepository
from backend.services.product_catalog.product_service import ProductService
from backend.repositories.product_catalog.category_repository import CategoryRepository
from backend.services.product_catalog.category_service import CategoryService

app = Flask(__name__)

@app.route('/add-product', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data['name']
    price = data['price']
    description = data['description']
    category = data['category']

    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="mydatabase"
    )

    product_repository = ProductRepository(db_connection)
    product_service = ProductService(product_repository)
    result = product_service.add_product(name, price, description, category)

    if result:
        return jsonify({'error': result}), 400

    return jsonify({'message': 'Product added successfully'}), 201

@app.route('/update-product', methods=['PUT'])
def update_product():
    data = request.get_json()
    product_id = data['product_id']
    price = data.get('price')
    description = data.get('description')
    category = data.get('category')

    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="mydatabase"
    )

    product_repository = ProductRepository(db_connection)
    product_service = ProductService(product_repository)
    result = product_service.update_product(product_id, price, description, category)

    if result:
        return jsonify({'error': result}), 400

    return jsonify({'message': 'Product updated successfully'}), 200

@app.route('/delete-product', methods=['DELETE'])
def delete_product():
    data = request.get_json()
    product_id = data['product_id']
    confirmation = data.get('confirmation')

    if not confirmation or confirmation != 'yes':
        return jsonify({'error': 'Product deletion not confirmed'}), 400

    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="mydatabase"
    )

    product_repository = ProductRepository(db_connection)
    product_service = ProductService(product_repository)
    product_service.delete_product(product_id)

    return jsonify({'message': 'Product deleted successfully'}), 200

@app.route('/search-products', methods=['GET'])
def search_products():
    term = request.args.get('term')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="mydatabase"
    )

    product_repository = ProductRepository(db_connection)
    product_service = ProductService(product_repository)
    products = product_service.search_products(term, page, per_page)

    return jsonify({'products': products}), 200

@app.route('/add-category', methods=['POST'])
def add_category():
    data = request.get_json()
    name = data['name']
    parent_id = data.get('parent_id')

    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="mydatabase"
    )

    category_repository = CategoryRepository(db_connection)
    category_service = CategoryService(category_repository)
    result = category_service.add_category(name, parent_id)
    
    if result:
        return jsonify({'error': result}), 400

    return jsonify({'message': 'Category added successfully'}), 201

@app.route('/update-category', methods=['PUT'])
def update_category():
    data = request.get_json()
    category_id = data['category_id']
    name = data['name']
    parent_id = data.get('parent_id')

    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="mydatabase"
    )

    category_repository = CategoryRepository(db_connection)
    category_service = CategoryService(category_repository)
    result = category_service.update_category(category_id, name, parent_id)
    
    if result:
        return jsonify({'error': result}), 400

    return jsonify({'message': 'Category updated successfully'}), 200

@app.route('/delete-category', methods=['DELETE'])
def delete_category():
    data = request.get_json()
    category_id = data['category_id']
    confirmation = data.get('confirmation')

    if not confirmation or confirmation != 'yes':
        return jsonify({'error': 'Category deletion not confirmed'}), 400

    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="mydatabase"
    )

    category_repository = CategoryRepository(db_connection)
    category_service = CategoryService(category_repository)
    category_service.delete_category(category_id)

    return jsonify({'message': 'Category deleted successfully'}), 200

@app.route('/categories', methods=['GET'])
def get_categories():
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="mydatabase"
    )

    category_repository = CategoryRepository(db_connection)
    category_service = CategoryService(category_repository)
    categories = category_service.get_all_categories()

    return jsonify({'categories': categories}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)