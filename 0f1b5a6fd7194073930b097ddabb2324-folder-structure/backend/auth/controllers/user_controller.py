from flask import Blueprint, request, jsonify, session
from flask_login import login_user, logout_user, login_required
from backend.auth.models.user import User
from backend.auth.extensions import db, bcrypt

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already exists"}), 400

    if not password or len(password) < 8:
        return jsonify({"error": "Password must be at least 8 characters long"}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    user = User.query.filter_by(email=email).first()

    if user is None or not bcrypt.check_password_hash(user.password, password):
        user.invalid_login_attempts += 1
        if user.invalid_login_attempts >= 5:
            user.is_active = False
            db.session.commit()
            return jsonify({"error": "Account locked due to too many invalid login attempts"}), 403
        db.session.commit()
        return jsonify({"error": "Invalid email or password"}), 401

    if not user.is_active:
        return jsonify({"error": "Account is locked. Please contact support."}), 403

    user.invalid_login_attempts = 0
    db.session.commit()

    login_user(user, remember=True)
    session.permanent = True

    return jsonify({"message": "Login successful", "user": {"email": user.email}}), 200

@auth_blueprint.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out successfully"}), 200