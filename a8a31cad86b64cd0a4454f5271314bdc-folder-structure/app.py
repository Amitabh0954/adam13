# Epic Title: User Account Management

from flask import Flask
from backend.user_account_management.controllers.user_controller import user_bp
from backend.user_account_management.controllers.password_reset_controller import password_reset_bp
from backend.database import engine, Base
from backend.product_catalog_management.controllers.product_controller import product_bp
from backend.shopping_cart_management.controllers.shopping_cart_controller import shopping_cart_bp

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Choose a secure key for production

# Register Blueprints
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(password_reset_bp, url_prefix='/auth')
app.register_blueprint(product_bp, url_prefix='/products')
app.register_blueprint(shopping_cart_bp, url_prefix='/cart')

# Create tables
Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    app.run(debug=True)