# Epic Title: User Account Management
from flask import Blueprint, request, jsonify
from services.user_session_service import UserSessionService
from flask_login import login_user

user_login_bp = Blueprint('user_login', __name__)
user_session_service = UserSessionService()

@user_login_bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({"error": "Email and Password are required"}), 400

    user = user_session_service.authenticate_user(email, password)
    
    if user is None:
        return jsonify({"error": "Invalid email or password"}), 401

    login_user(user)
    return jsonify({"message": "Logged in successfully"}), 200