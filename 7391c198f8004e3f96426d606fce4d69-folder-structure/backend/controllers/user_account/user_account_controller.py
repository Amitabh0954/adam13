from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from backend.repositories.user_account.user_repository import UserRepository

user_account_controller = Blueprint('user_account_controller', __name__)
user_repo = UserRepository()

@user_account_controller.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    first_name = data.get('first_name', '')
    last_name = data.get('last_name', '')

    if user_repo.get_user_by_email(email):
        return jsonify({"error": "Email already registered"}), 400

    if not validate_password(password):
        return jsonify({"error": "Password does not meet security criteria"}), 400

    hashed_password = generate_password_hash(password)
    new_user = user_repo.create_user(email, hashed_password, first_name, last_name)

    return jsonify({"message": "User registered successfully"}), 201

def validate_password(password: str) -> bool:
    if len(password) < 8 or not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
        return False
    return True