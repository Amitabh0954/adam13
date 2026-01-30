# Epic Title: User Account Management
from flask import Blueprint, request, jsonify
from services.user_service import UserService
import re

user_registration_bp = Blueprint('user_registration', __name__)
user_service = UserService()

@user_registration_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    # Validate email format
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    if not re.match(email_regex, email):
        return jsonify({"error": "Invalid email format"}), 400

    # Validate password security
    if len(password) < 8:
        return jsonify({"error": "Password must be at least 8 characters long"}), 400
    if not re.search(r"[a-z]", password) or not re.search(r"[A-Z]", password) or not re.search(r"[0-9]", password):
        return jsonify({"error": "Password must contain at least one lowercase letter, one uppercase letter, and one digit"}), 400

    response = user_service.register_user(email, password)

    if response.get("error"):
        return jsonify(response), 400
    
    return jsonify(response), 201