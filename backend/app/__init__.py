from flask import Flask
from backend.app.routes.routes import register_routes
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.repositories.user_account.models.user import Base as UserBase

def create_app():
    app = Flask(__name__)

    # Initialize the database
    user_engine = create_engine('mysql+pymysql://username:password@localhost:3306/databasename')
    UserSession = sessionmaker(bind=user_engine)
    UserBase.metadata.create_all(user_engine)

    # Register routes
    register_routes(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

#### 8. Update requirements.txt with necessary dependencies

##### Requirements File