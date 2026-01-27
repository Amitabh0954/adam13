# Epic Title: User Account Management

from flask import Blueprint, request, jsonify
from backend.user_account_management.services.user_service import UserService
from werkzeug.security import generate_password_hash

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400

    if len(password) < 8:
        return jsonify({'message': 'Password must be at least 8 characters long'}), 400

    hashed_password = generate_password_hash(password, method='sha256')
    user_service = UserService()
    result = user_service.create_user(email, hashed_password)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'User registered successfully'}), 201