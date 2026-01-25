from flask import Flask
from backend.app.routes.routes import register_routes
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.repositories.product_catalog.models.product import Base as ProductBase

def create_app():
    app = Flask(__name__)

    # Initialize the database
    product_engine = create_engine('mysql+pymysql://username:password@localhost:3306/databasename')
    ProductSession = sessionmaker(bind=product_engine)
    ProductBase.metadata.create_all(product_engine)

    # Register routes
    register_routes(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

#### 7. Update requirements.txt if any new dependencies are required