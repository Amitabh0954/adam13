# Epic Title: User Account Management
from flask import Blueprint, request, jsonify
from backend.services.user_account.login_service import LoginService

login_bp = Blueprint('login', __name__)
login_service = LoginService()

@login_bp.route('/api/user_account/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    response = login_service.login(email, password)
    if "error" in response:
        return jsonify(response), 400

    return jsonify(response), 200

@login_bp.route('/api/user_account/validate_session', methods=['GET'])
def validate_session():
    session_token = request.args.get('session_token')

    if not session_token:
        return jsonify({"error": "Session token is required"}), 400

    is_valid = login_service.validate_session(session_token)

    if not is_valid:
        return jsonify({"error": "Invalid or expired session"}), 401

    return jsonify({"message": "Session is valid"}), 200