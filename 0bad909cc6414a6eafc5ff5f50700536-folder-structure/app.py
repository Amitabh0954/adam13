# Epic Title: Product Catalog Management

from flask import Flask, request, jsonify
import mysql.connector
from backend.repositories.product_catalog.product_repository import ProductRepository
from backend.services.product_catalog.product_service import ProductService

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)