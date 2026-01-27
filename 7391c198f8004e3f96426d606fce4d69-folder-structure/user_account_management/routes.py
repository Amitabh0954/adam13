from flask import request, jsonify, session
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash
from . import user_blueprint
from .models import User
from .extensions import db
from .utils import validate_password

MAX_LOGIN_ATTEMPTS = 5

@user_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    first_name = data.get('first_name', '')
    last_name = data.get('last_name', '')

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already registered"}), 400

    if not validate_password(password):
        return jsonify({"error": "Password does not meet security criteria"}), 400

    hashed_password = generate_password_hash(password)
    new_user = User(email=email, password=hashed_password, first_name=first_name, last_name=last_name)

    db.session.add(new_user)
    db.session.commit()

    login_user(new_user)
    return jsonify({"message": "User registered successfully"}), 201

@user_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    
    if user is None or not check_password_hash(user.password, password):
        if user:
            user.invalid_login_attempts += 1
            db.session.commit()
            if user.invalid_login_attempts >= MAX_LOGIN_ATTEMPTS:
                return jsonify({"error": "Too many invalid login attempts"}), 403
        return jsonify({"error": "Invalid credentials"}), 401

    user.invalid_login_attempts = 0
    user.last_login_at = user.current_login_at
    user.current_login_at = datetime.datetime.utcnow()
    user.login_count += 1
    db.session.commit()

    login_user(user)
    session.permanent = True
    return jsonify({"message": "Login successful"}), 200

@user_blueprint.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return jsonify({"message": "Logged out successfully"}), 200