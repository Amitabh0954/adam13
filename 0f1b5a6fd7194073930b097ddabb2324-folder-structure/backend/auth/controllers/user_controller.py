from flask import Blueprint, request, jsonify, url_for
from flask_login import login_user, logout_user, login_required
from itsdangerous import URLSafeTimedSerializer
from backend.auth.models.user import User, PasswordResetToken
from backend.auth.extensions import db, bcrypt, mail

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

@auth_blueprint.route('/request_password_reset', methods=['POST'])
def request_password_reset():
    data = request.get_json()
    email = data.get('email')

    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({"error": "Email not found"}), 404

    token = generate_password_reset_token(user.email)
    reset_url = url_for('auth.reset_password', token=token, _external=True)
    html = f'<p>Click the link below to reset your password:</p><p><a href="{reset_url}">{reset_url}</a></p>'
    
    send_email(user.email, 'Password Reset Request', html)
    
    return jsonify({"message": "Password reset link has been sent to your email"}), 200

@auth_blueprint.route('/reset_password/<token>', methods=['POST'])
def reset_password(token):
    data = request.get_json()
    password = data.get('password')

    if not password or len(password) < 8:
        return jsonify({"error": "Password must be at least 8 characters long"}), 400

    email = confirm_password_reset_token(token)
    if not email:
        return jsonify({"error": "Invalid or expired token"}), 400

    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({"error": "User not found"}), 404

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    user.password = hashed_password
    db.session.commit()

    return jsonify({"message": "Password reset successfully"}), 200

def generate_password_reset_token(email: str) -> str:
    serializer = URLSafeTimedSerializer(Config.SECRET_KEY)
    return serializer.dumps(email, salt='password-reset-salt')

def confirm_password_reset_token(token: str, expiration=86400) -> str | None:
    serializer = URLSafeTimedSerializer(Config.SECRET_KEY)
    try:
        email = serializer.loads(token, salt='password-reset-salt', max_age=expiration)
        return email
    except:
        return None

def send_email(to: str, subject: str, html: str):
    from flask_mail import Message
    msg = Message(subject, recipients=[to], html=html)
    mail.send(msg)