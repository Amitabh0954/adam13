# Epic Title: User Account Management

from flask import Flask
from structured_logging import setup_logging
from backend.user_account_management.controllers.profile_controller import profile_blueprint

def create_app() -> Flask:
    app = Flask(__name__)
    
    setup_logging()
    
    app.register_blueprint(profile_blueprint, url_prefix='/api/v1')
    
    @app.before_first_request
    def initialize_database():
        from backend.user_account_management.models.user import Base as UserBase
        from backend.user_account_management.models.session import Base as SessionBase
        from backend.user_account_management.models.password_reset import Base as PasswordResetBase
        from backend.user_account_management.models.profile import Base as ProfileBase
        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker
        
        engine = create_engine('mysql+pymysql://user:password@localhost/dbname')
        UserBase.metadata.create_all(engine)
        SessionBase.metadata.create_all(engine)
        PasswordResetBase.metadata.create_all(engine)
        ProfileBase.metadata.create_all(engine)
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