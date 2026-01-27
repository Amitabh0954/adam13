# Epic Title: Product Catalog Management

from flask import Flask
from backend.product_catalog_management.controllers.product_controller import product_bp
from backend.database import engine, Base

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Choose a secure key for production

# Register Blueprints
app.register_blueprint(product_bp, url_prefix='/products')

# Create tables
Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    app.run(debug=True)