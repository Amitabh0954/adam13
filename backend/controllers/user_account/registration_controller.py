from flask import Blueprint, request, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from backend.services.user_account.registration_service import RegistrationService
from backend.services.user_account.schemas.user_schema import UserSchema

engine = create_engine('mysql+pymysql://username:password@localhost:3306/databasename')
Session = sessionmaker(bind=engine)

registration_controller = Blueprint('registration_controller', __name__)

@registration_controller.route('/register', methods=['POST'])
def register_user():
    session = Session()
    registration_service = RegistrationService(session)

    try:
        data = request.json
        user = registration_service.register_user(data)
        user_schema = UserSchema()
        return jsonify(user_schema.dump(user)), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

##### User Schema (for serialization)