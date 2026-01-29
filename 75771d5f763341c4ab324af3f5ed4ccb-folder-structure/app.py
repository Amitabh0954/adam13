# Epic Title: Save Shopping Cart for Logged-in Users

from flask import Flask
from backend.controllers.shopping_cart.shopping_cart_save_controller import shopping_cart_save_controller

def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(shopping_cart_save_controller, url_prefix='/api')
    
    # Additional setup such as logging and lifecycle hooks can be added here
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)