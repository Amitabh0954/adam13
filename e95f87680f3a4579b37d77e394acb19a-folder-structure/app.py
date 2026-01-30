# Epic Title: Product Catalog Management
from flask import Flask, request, jsonify
from backend.services.product_catalog_management.add_product_service import AddProductService
from backend.services.product_catalog_management.update_product_service import UpdateProductService

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'

add_product_service = AddProductService()
update_product_service = UpdateProductService()

@app.route('/api/product_catalog_management/add_product', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    category = data.get('category')

    if not name or not description or price is None:
        return jsonify({"error": "Name, description, and price are required"}), 400
    
    response = add_product_service.add_product(name, description, price, category)

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

@app.route('/')
def index():
    return "Welcome to the Product Catalog Management System"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)