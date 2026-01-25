from flask import Blueprint, request, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from backend.services.shopping_cart.shopping_cart_service import ShoppingCartService

engine = create_engine('mysql+pymysql://username:password@localhost:3306/databasename')
Session = sessionmaker(bind=engine)

shopping_cart_controller = Blueprint('shopping_cart_controller', __name__)

@shopping_cart_controller.route('/cart', methods=['POST'])
def add_product_to_cart():
    session_db = Session()
    shopping_cart_service = ShoppingCartService(session_db)

    user_id = request.json.get('user_id')
    session_id = request.json.get('session_id')
    product_id = request.json.get('product_id')
    quantity = int(request.json.get('quantity', 1))
    price = float(request.json.get('price'))

    try:
        cart_item = shopping_cart_service.add_product_to_cart(user_id, session_id, product_id, quantity, price)
        return jsonify({"message": "Product added to cart successfully", "cart_item_id": cart_item.id}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@shopping_cart_controller.route('/cart/remove', methods=['DELETE'])
def remove_product_from_cart():
    session_db = Session()
    shopping_cart_service = ShoppingCartService(session_db)

    user_id = request.json.get('user_id')
    session_id = request.json.get('session_id')
    product_id = request.json.get('product_id')

    try:
        cart = shopping_cart_service.remove_product_from_cart(user_id, session_id, product_id)
        return jsonify({"message": "Product removed from cart successfully", "total_price": cart.total_price}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

#### 5. Update routes to include endpoints for removing products from the shopping cart