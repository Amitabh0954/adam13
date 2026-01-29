# Epic Title: Product Categorization

from flask import Flask
from backend.controllers.product_catalog.category_controller import category_controller

def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(category_controller, url_prefix='/api')
    
    # Additional setup such as logging and lifecycle hooks can be added here
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)