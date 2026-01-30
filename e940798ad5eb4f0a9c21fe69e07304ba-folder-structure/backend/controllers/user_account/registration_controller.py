# Epic Title: User Account Management
from flask import Blueprint, request, jsonify
from backend.services.user_account.user_service import UserService

registration_bp = Blueprint('registration', __name__)
user_service = UserService()

@registration_bp.route('/api/user_account/register', methods=['POST'])
def register_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    response = user_service.register_user(email, password)
    if "error" in response:
        return jsonify(response), 400

    return jsonify(response), 200