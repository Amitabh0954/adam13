from flask import Blueprint, request, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from flask_mail import Mail
from backend.services.user_account.password_reset_service.py import PasswordResetService
from backend.services.user_account.schemas.user_schema import UserSchema

engine = create_engine('mysql+pymysql://username:password@localhost:3306/databasename')
Session = sessionmaker(bind=engine)
mail = Mail()

password_reset_controller = Blueprint('password_reset_controller', __name__)

@password_reset_controller.route('/request_password_reset', methods=['POST'])
def request_password_reset():
    session_db = Session()
    password_reset_service = PasswordResetService(session_db, mail)

    try:
        data = request.json
        password_reset_service.generate_reset_token(data['email'])
        return jsonify({"message": "Password reset link sent to your email"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@password_reset_controller.route('/reset_password', methods=['POST'])
def reset_password():
    session_db = Session()
    password_reset_service = PasswordResetService(session_db, mail)

    try:
        data = request.json
        password_reset_service.reset_password(data['token'], data['new_password'])
        return jsonify({"message": "Password has been reset successfully"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

#### 5. Update routes to include the new password reset and verification endpoints