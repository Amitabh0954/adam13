from flask import Blueprint, request, jsonify, session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from backend.services.user_account.login_service import LoginService
from backend.services.user_account.schemas.user_schema import UserSchema

engine = create_engine('mysql+pymysql://username:password@localhost:3306/databasename')
Session = sessionmaker(bind=engine)

login_controller = Blueprint('login_controller', __name__)

@login_controller.route('/login', methods=['POST'])
def login_user():
    session_db = Session()
    login_service = LoginService(session_db)

    try:
        data = request.json
        user = login_service.login_user(data['email'], data['password'])
        user_schema = UserSchema()
        return jsonify(user_schema.dump(user)), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

##### User Schema (for serialization)