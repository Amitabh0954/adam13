from flask import Flask
from backend.controllers.shopping_cart.shopping_cart_controller import shopping_cart_controller

def register_routes(app: Flask):
    app.register_blueprint(shopping_cart_controller, url_prefix='/api')

#### 6. Ensure this feature works by initializing it in the application