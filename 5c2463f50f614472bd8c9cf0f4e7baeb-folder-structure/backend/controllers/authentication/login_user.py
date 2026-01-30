# Epic Title: User Account Management
from flask import Blueprint, request, jsonify
from flask_login import login_user
from services.authentication.login_service import LoginService

login_user_bp = Blueprint('login_user', __name__)
login_service = LoginService()

@login_user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    user, error = login_service.login_user(email, password)

    if error:
        return jsonify({"error": error}), 400

    login_user(user)
    return jsonify({"message": "Logged in successfully"}), 200