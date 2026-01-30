# Epic Title: User Account Management
from flask import Blueprint, request, jsonify
from services.user_registration_service import UserRegistrationService

user_registration_bp = Blueprint('user_registration', __name__)
registration_service = UserRegistrationService()

@user_registration_bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    response = registration_service.register_user(email, password)
    if response.get("error"):
        return jsonify(response), 400
    
    return jsonify(response), 201