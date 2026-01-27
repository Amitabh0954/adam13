from flask import request, jsonify, session, url_for
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from itsdangerous import URLSafeTimedSerializer
from datetime import datetime, timedelta
from . import user_blueprint
from .models import User, PasswordResetToken
from .extensions import db, mail
from .utils import validate_password, send_email

MAX_LOGIN_ATTEMPTS = 5
TOKEN_EXPIRATION_HOURS = 24

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
    user.current_login_at = datetime.now()
    user.login_count += 1
    db.session.commit()

    login_user(user)
    session.permanent = True
    return jsonify({"message": "Login successful"}), 200

@user_blueprint.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return jsonify({"message": "Logged out successfully"}), 200

@user_blueprint.route('/reset_password_request', methods=['POST'])
def reset_password_request():
    data = request.get_json()
    email = data.get('email')

    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({"error": "Email not found"}), 404

    token_serializer = URLSafeTimedSerializer(Config.SECRET_KEY)
    token = token_serializer.dumps(email, salt='password-reset-salt')

    expires_at = datetime.now() + timedelta(hours=TOKEN_EXPIRATION_HOURS)
    password_reset_token = PasswordResetToken(user=user, token=token, expires_at=expires_at)
    db.session.add(password_reset_token)
    db.session.commit()

    reset_url = url_for('user.reset_password', token=token, _external=True)
    send_email(
        subject="Password Reset Request",
        recipients=[email],
        text_body=f"Click to reset your password: {reset_url}",
        html_body=f'<p>Click to reset your password: <a href="{reset_url}">{reset_url}</a></p>'
    )

    return jsonify({"message": "Password reset email sent"}), 200

@user_blueprint.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if request.method == 'POST':
        data = request.get_json()
        new_password = data.get('password')

        if not validate_password(new_password):
            return jsonify({"error": "Password does not meet security criteria"}), 400

        password_reset_token = PasswordResetToken.query.filter_by(token=token).first()
        if not password_reset_token or password_reset_token.expires_at < datetime.now():
            return jsonify({"error": "Invalid or expired token"}), 400

        user = password_reset_token.user
        user.password = generate_password_hash(new_password)

        db.session.delete(password_reset_token)
        db.session.commit()

        return jsonify({"message": "Password reset successful"}), 200

    return jsonify({"message": "Please provide a new password"}), 200