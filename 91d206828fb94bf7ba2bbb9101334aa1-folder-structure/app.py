# Epic Title: Shopping Cart Functionality
from flask import Flask
from datetime import timedelta
from backend.user_account.routes.user_registration import user_registration_bp
from backend.user_session.routes.user_login import user_login_bp
from backend.user_account.routes.password_recovery import password_recovery_bp
from backend.user_account.routes.profile_management import profile_management_bp
from backend.product_catalog.routes.add_product import add_product_bp
from backend.product_catalog.routes.update_product import update_product_bp
from backend.product_catalog.routes.delete_product import delete_product_bp
from backend.product_catalog.routes.search_product import search_product_bp
from backend.product_catalog.routes.manage_categories import manage_categories_bp
from backend.shopping_cart.routes.add_to_cart import add_to_cart_bp
from backend.shopping_cart.routes.remove_from_cart import remove_from_cart_bp
from backend.shopping_cart.routes.modify_cart_quantity import modify_cart_quantity_bp
from backend.shopping_cart.routes.save_cart import save_cart_bp
from flask_login import LoginManager

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'supersecretkey'
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        from backend.user_session.models.user import User
        return User(user_id, "placeholder_email")

    app.register_blueprint(user_registration_bp, url_prefix='/api/user_account')
    app.register_blueprint(user_login_bp, url_prefix='/api/user_session')
    app.register_blueprint(password_recovery_bp, url_prefix='/api/user_account')
    app.register_blueprint(profile_management_bp, url_prefix='/api/user_account')
    app.register_blueprint(add_product_bp, url_prefix='/api/product_catalog')
    app.register_blueprint(update_product_bp, url_prefix='/api/product_catalog')
    app.register_blueprint(delete_product_bp, url_prefix='/api/product_catalog')
    app.register_blueprint(search_product_bp, url_prefix='/api/product_catalog')
    app.register_blueprint(manage_categories_bp, url_prefix='/api/product_catalog')
    app.register_blueprint(add_to_cart_bp, url_prefix='/api/shopping_cart')
    app.register_blueprint(remove_from_cart_bp, url_prefix='/api/shopping_cart')
    app.register_blueprint(modify_cart_quantity_bp, url_prefix='/api/shopping_cart')
    app.register_blueprint(save_cart_bp, url_prefix='/api/shopping_cart')

    @app.route('/')
    def index():
        return "Welcome to the Shopping Cart Management System"

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)