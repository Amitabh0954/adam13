# Epic Title: Shopping Cart Functionality

from flask import Flask, session
from backend.product_catalog_management.controllers.product_controller import product_bp
from backend.product_catalog_management.controllers.category_controller import category_bp
from backend.shopping_cart_functionality.controllers.cart_controller import cart_bp
from backend.database import engine, Base

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Choose a secure key for production

# Register Blueprints
app.register_blueprint(product_bp, url_prefix='/products')
app.register_blueprint(category_bp, url_prefix='/categories')
app.register_blueprint(cart_bp, url_prefix='/cart')

# Create tables
Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    app.run(debug=True)