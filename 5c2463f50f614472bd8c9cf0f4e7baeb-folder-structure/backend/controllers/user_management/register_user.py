# Epic Title: User Account Management
from flask import Blueprint, request, jsonify
from services.user_management.registration_service import RegistrationService

register_user_bp = Blueprint('register_user', __name__)
registration_service = RegistrationService()

@register_user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    response = registration_service.register_user(email, password)

    if response.get("error"):
        return jsonify(response), 400
    
    return jsonify(response), 201