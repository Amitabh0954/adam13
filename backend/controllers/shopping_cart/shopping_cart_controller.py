from flask import Blueprint, request, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from backend.services.shopping_cart.shopping_cart_service import ShoppingCartService

engine = create_engine('mysql+pymysql://username:password@localhost:3306/databasename')
Session = sessionmaker(bind=engine)

shopping_cart_controller = Blueprint('shopping_cart_controller', __name__)

@shopping_cart_controller.route('/cart/save', methods=['POST'])
def save_shopping_cart():
    session_db = Session()
    shopping_cart_service = ShoppingCartService(session_db)

    user_id = request.json.get('user_id')
    session_id = request.json.get('session_id')

    try:
        shopping_cart_service.save_shopping_cart(user_id, session_id)
        return jsonify({"message": "Shopping cart saved successfully"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@shopping_cart_controller.route('/cart/retrieve', methods=['GET'])
def retrieve_shopping_cart():
    session_db = Session()
    shopping_cart_service = ShoppingCartService(session_db)

    user_id = request.args.get('user_id')

    try:
        cart_data = shopping_cart_service.retrieve_shopping_cart(user_id)
        return jsonify({"cart": cart_data}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

#### 5. Update routes to include endpoints for saving and retrieving the shopping cart state