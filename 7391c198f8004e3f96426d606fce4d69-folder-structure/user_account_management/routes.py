from flask import request, jsonify, session, url_for
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from . import user_blueprint
from .models import User, PasswordResetToken
from .extensions import db
from .utils import send_password_reset_email, get_password_reset_token, validate_password_reset_token

@user_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    
    if user and check_password_hash(user.password, password):
        session.permanent = True
        login_user(user)
        return jsonify({"message": "Logged in successfully"}), 200
    else:
        record_invalid_login_attempt(email)
        return jsonify({"error": "Invalid email or password"}), 401

@user_blueprint.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out successfully"}), 200

@user_blueprint.route('/reset_password', methods=['POST'])
def reset_password_request():
    email = request.json.get('email')
    user = User.query.filter_by(email=email).first()
    if user:
        token = get_password_reset_token(user)
        send_password_reset_email(user.email, token)
    return jsonify({"message": "If an account with that email exists, a reset link has been sent."}), 200

@user_blueprint.route('/reset_password/<token>', methods=['POST'])
def reset_password(token):
    user = validate_password_reset_token(token)
    if not user:
        return jsonify({"error": "Invalid or expired token"}), 401
    data = request.get_json()
    new_password = data.get('password')
    if not validate_password(new_password):
        return jsonify({"error": "Password does not meet security criteria"}), 400

    user.password = generate_password_hash(new_password)
    db.session.commit()
    return jsonify({'message': 'Password has been updated!'}), 200

@user_blueprint.route('/profile', methods=['GET', 'PUT'])
@login_required
def profile():
    if request.method == 'GET':
        return jsonify({
            "email": current_user.email,
            "first_name": current_user.first_name,
            "last_name": current_user.last_name
        }), 200

    if request.method == 'PUT':
        data = request.get_json()
        current_user.first_name = data.get('first_name', current_user.first_name)
        current_user.last_name = data.get('last_name', current_user.last_name)
        db.session.commit()
        return jsonify({"message": "Profile updated successfully"}), 200

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def record_invalid_login_attempt(email: str):
    # Here you would implement your logic to track the invalid attempts and lock the account if needed.
    pass

@user_blueprint.before_request
def before_request():
    session.modified = True

def validate_password(password: str) -> bool:
    if len(password) < 8 or not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
        return False
    return True