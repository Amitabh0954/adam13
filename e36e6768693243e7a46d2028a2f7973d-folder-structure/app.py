# Epic Title: Product Catalog Management

from flask import Flask
from backend.controllers.product_controller import product_bp
from backend.controllers.category_controller import category_bp
from backend.database import engine, Base

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Choose a secure key for production

# Register Blueprints
app.register_blueprint(product_bp, url_prefix='/products')
app.register_blueprint(category_bp, url_prefix='/categories')

# Create tables
Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    app.run(debug=True)