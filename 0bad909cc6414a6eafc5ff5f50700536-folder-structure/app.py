# Epic Title: Shopping Cart Functionality

from flask import Flask, request, jsonify, session
import mysql.connector
from backend.repositories.shopping_cart.shopping_cart_repository import ShoppingCartRepository
from backend.services.shopping_cart.shopping_cart_service import ShoppingCartService

app = Flask(__name__)
app.secret_key = 'super_secret_key'

@app.route('/add-to-cart', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    user_id = session.get('user_id')
    product_id = data['product_id']
    quantity = data['quantity']

    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="mydatabase"
    )

    shopping_cart_repository = ShoppingCartRepository(db_connection)
    shopping_cart_service = ShoppingCartService(shopping_cart_repository)
    result = shopping_cart_service.add_product_to_cart(user_id, product_id, quantity)

    if result:
        return jsonify({'error': result}), 400

    return jsonify({'message': 'Product added to cart successfully'}), 201

@app.route('/view-cart', methods=['GET'])
def view_cart():
    user_id = session.get('user_id')

    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="mydatabase"
    )

    shopping_cart_repository = ShoppingCartRepository(db_connection)
    shopping_cart_service = ShoppingCartService(shopping_cart_repository)
    cart_items = shopping_cart_service.get_cart_items(user_id)

    return jsonify({'cart_items': cart_items}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)