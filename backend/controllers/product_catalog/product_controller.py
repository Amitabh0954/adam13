from flask import Blueprint, request, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from backend.services.product_catalog.product_service import ProductService

engine = create_engine('mysql+pymysql://username:password@localhost:3306/databasename')
Session = sessionmaker(bind=engine)

product_controller = Blueprint('product_controller', __name__)

@product_controller.route('/products/search', methods=['GET'])
def search_products():
    session_db = Session()
    product_service = ProductService(session_db)

    search_term = request.args.get('search_term', '')
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', 10))

    try:
        results = product_service.search_products(search_term, page, page_size)
        return jsonify({"products": results}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

#### 5. Update routes to include the new product search endpoint