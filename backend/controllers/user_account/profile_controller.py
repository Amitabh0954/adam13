from flask import Blueprint, request, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from backend.services.user_account.profile_service import ProfileService
from backend.services.user_account.schemas.user_schema import UserSchema

engine = create_engine('mysql+pymysql://username:password@localhost:3306/databasename')
Session = sessionmaker(bind=engine)

profile_controller = Blueprint('profile_controller', __name__)

@profile_controller.route('/profile/<int:user_id>', methods=['PUT'])
def update_profile(user_id):
    session_db = Session()
    profile_service = ProfileService(session_db)

    try:
        data = request.json
        user = profile_service.update_profile(user_id, data)
        user_schema = UserSchema()
        return jsonify(user_schema.dump(user)), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

##### User Schema (for serialization)