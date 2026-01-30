# Epic Title: Product Catalog Management
from flask import Flask, session
from backend.product_catalog.routes.add_product import add_product_bp
from backend.product_catalog.routes.update_product import update_product_bp
from backend.product_catalog.routes.delete_product import delete_product_bp
from backend.product_catalog.routes.search_product import search_product_bp

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'supersecretkey'
    app.config['PERMANENT_SESSION_LIFETIME'] = 1800  # Session will timeout after 30 minutes of inactivity
    
    app.register_blueprint(add_product_bp, url_prefix='/api/product_catalog')
    app.register_blueprint(update_product_bp, url_prefix='/api/product_catalog')
    app.register_blueprint(delete_product_bp, url_prefix='/api/product_catalog')
    app.register_blueprint(search_product_bp, url_prefix='/api/product_catalog')
    
    @app.route('/')
    def index():
        return "Welcome to the Product Catalog Management System"

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)