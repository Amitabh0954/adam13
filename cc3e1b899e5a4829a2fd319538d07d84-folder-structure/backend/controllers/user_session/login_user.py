# Epic Title: User Account Management
from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user
from services.user_session.login_service import LoginService

login_user_bp = Blueprint('login_user', __name__)
login_service = LoginService()

@login_user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    user = login_service.authenticate_user(email, password)
    if not user:
        return jsonify({"error": "Invalid email or password"}), 400
    
    login_user(user)
    return jsonify({"message": "Logged in successfully"}), 200

@login_user_bp.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return jsonify({"message": "Logged out successfully"}), 200