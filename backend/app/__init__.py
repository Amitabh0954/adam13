from flask import Flask
from backend.app.routes.routes import register_routes
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.repositories.shopping_cart.models.shopping_cart import Base as ShoppingCartBase
from backend.repositories.shopping_cart.models.shopping_cart_item import Base as ShoppingCartItemBase
from backend.repositories.product_catalog.models.product import Base as ProductBase

def create_app():
    app = Flask(__name__)

    # Initialize the database
    shopping_cart_engine = create_engine('mysql+pymysql://username:password@localhost:3306/databasename')
    ProductSession = sessionmaker(bind=shopping_cart_engine)
    ShoppingCartBase.metadata.create_all(shopping_cart_engine)
    ShoppingCartItemBase.metadata.create_all(shopping_cart_engine)
    ProductBase.metadata.create_all(shopping_cart_engine)

    # Register routes
    register_routes(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

#### 8. Update requirements.txt if any new dependencies are required