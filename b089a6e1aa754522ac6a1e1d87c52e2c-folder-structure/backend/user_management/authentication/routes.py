import logging
from datetime import datetime, timedelta
from uuid import uuid4
from flask import Blueprint, request, jsonify, session, render_template, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from .models import db, User, PasswordResetToken
from flask_mail import Mail, Message

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

auth_bp = Blueprint('auth_bp', __name__)
MAX_FAILED_ATTEMPTS = 5
LOCK_DURATION = timedelta(minutes=15)
SESSION_TIMEOUT = 1800  # in seconds (30 minutes)
TOKEN_EXPIRATION = timedelta(hours=24)

mail = Mail()

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400

    if User.query.filter_by(email=email).first() is not None:
        return jsonify({'message': 'Email already registered'}), 400

    password_hash = generate_password_hash(password)
    new_user = User(email=email, password_hash=password_hash)
    db.session.add(new_user)
    db.session.commit()

    logger.info(f"User {email} registered successfully")
    return jsonify({'message': 'User registered successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if user is None or not user.is_active:
        return jsonify({'message': 'Invalid email or account disabled'}), 400

    if user.account_locked_until and user.account_locked_until > datetime.utcnow():
        return jsonify({'message': 'Account is locked. Try again later.'}), 403

    if not check_password_hash(user.password_hash, password):
        user.failed_login_attempts += 1
        if user.failed_login_attempts >= MAX_FAILED_ATTEMPTS:
            user.account_locked_until = datetime.utcnow() + LOCK_DURATION
            db.session.commit()
            return jsonify({'message': 'Account locked due to too many failed attempts. Try again later.'}), 403
        db.session.commit()
        return jsonify({'message': 'Invalid email or password'}), 400

    user.failed_login_attempts = 0
    db.session.commit()

    session['user_id'] = user.id
    session['last_activity'] = datetime.now().timestamp()

    logger.info(f"User {email} logged in successfully")
    return jsonify({'message': 'Logged in successfully'}), 200

@auth_bp.route('/password-reset', methods=['POST'])
def password_reset_request():
    data = request.get_json()
    email = data.get('email')

    user = User.query.filter_by(email=email).first()

    if user is None:
        return jsonify({'message': 'Email not found'}), 404

    token = str(uuid4())
    expires_at = datetime.utcnow() + TOKEN_EXPIRATION

    reset_token = PasswordResetToken(
        user_id=user.id,
        token=token,
        expires_at=expires_at
    )

    db.session.add(reset_token)
    db.session.commit()

    reset_url = url_for('auth_bp.password_reset_confirm', token=token, _external=True)
    send_password_reset_email(user.email, reset_url)

    logger.info(f"Password reset link sent to {email}")
    return jsonify({'message': 'Password reset link sent'}), 200

@auth_bp.route('/password-reset/<token>', methods=['GET', 'POST'])
def password_reset_confirm(token):
    reset_token = PasswordResetToken.query.filter_by(token=token).first()

    if reset_token is None or reset_token.expires_at < datetime.utcnow():
        return jsonify({'message': 'Invalid or expired token'}), 400

    if request.method == 'POST':
        data = request.get_json()
        password = data.get('password')

        if not password:
            return jsonify({'message': 'Password is required'}), 400

        user = User.query.get(reset_token.user_id)
        user.password_hash = generate_password_hash(password)

        db.session.delete(reset_token)
        db.session.commit()

        logger.info(f"User {user.email} has reset the password successfully")
        return jsonify({'message': 'Password reset successfully'}), 200

    return render_template('password_reset_confirm.html', token=token)

def send_password_reset_email(to_email, reset_url):
    msg = Message('Password Reset Request',
                  sender='noreply@yourapp.com',
                  recipients=[to_email])
    msg.body = fTo reset your password, visit the following link:
{reset_url}

If you did not make this request, simply ignore this email and no changes will be made.

    mail.send(msg)

@auth_bp.before_request
def before_request():
    session.permanent = True
    if 'user_id' in session:
        now = datetime.now().timestamp()
        if now - session.get('last_activity', 0) > SESSION_TIMEOUT:
            session.clear()
            return jsonify({'message': 'Session timed out, please log in again.'}), 403
        session['last_activity'] = now