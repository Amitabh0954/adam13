# Epic Title: Shopping Cart Functionality

from flask import Flask
from structured_logging import setup_logging
from backend.shopping_cart_functionality.controllers.cart_controller import cart_blueprint

def create_app() -> Flask:
    app = Flask(__name__)
    
    setup_logging()
    
    app.register_blueprint(cart_blueprint, url_prefix='/api/v1')
    
    @app.before_first_request
    def initialize_database():
        from backend.shopping_cart_functionality.models.cart import Base as CartBase
        from backend.shopping_cart_functionality.models.cart_item import Base as CartItemBase
        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker
        
        engine = create_engine('mysql+pymysql://user:password@localhost/dbname')
        CartBase.metadata.create_all(engine)
        CartItemBase.metadata.create_all(engine)
        session = sessionmaker(bind=engine)()
        app.config['db_session'] = session
    
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        session = app.config['db_session']
        session.remove()
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)