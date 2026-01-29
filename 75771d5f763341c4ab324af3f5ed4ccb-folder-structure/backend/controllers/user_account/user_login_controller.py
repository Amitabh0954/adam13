# Epic Title: User Login

from flask import Blueprint, request, jsonify
from services.user_account.user_login_service import UserLoginService
from validators.user_account.user_login_validator import UserLoginValidator

user_login_controller = Blueprint('user_login_controller', __name__)

@user_login_controller.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    validator = UserLoginValidator(data)
    if validator.is_valid():
        service = UserLoginService()
        response = service.login_user(data)
        if response:
            return jsonify(response), 200
    return jsonify(validator.errors), 400