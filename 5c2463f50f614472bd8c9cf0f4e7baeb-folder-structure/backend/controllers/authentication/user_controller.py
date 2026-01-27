from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.services.authentication.user_service import UserService
from backend.repositories.authentication.user_repository import UserRepository

auth_blueprint = Blueprint('auth', __name__)
user_service = UserService()

@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    try:
        user_service.register_user(email, password)
        return jsonify({"message": "User registered successfully"}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400