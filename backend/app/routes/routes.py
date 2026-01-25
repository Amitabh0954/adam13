from flask import Flask
from backend.controllers.product_catalog.product_controller import product_controller

def register_routes(app: Flask):
    app.register_blueprint(product_controller, url_prefix='/api')

#### 6. Ensure this feature works by initializing it in the application