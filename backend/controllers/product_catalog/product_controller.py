from flask import Blueprint, request, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from backend.services.product_catalog.product_service import ProductService

engine = create_engine('mysql+pymysql://username:password@localhost:3306/databasename')
Session = sessionmaker(bind=engine)

product_controller = Blueprint('product_controller', __name__)

@product_controller.route('/products', methods=['POST'])
def add_product():
    session_db = Session()
    product_service = ProductService(session_db)

    try:
        data = request.json
        product = product_service.add_product(data)
        return jsonify({"message": "Product added successfully", "product": product.name}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

#### 5. Update routes to include the new product addition endpoint