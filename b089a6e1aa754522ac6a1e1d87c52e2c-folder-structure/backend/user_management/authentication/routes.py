import logging
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from .models import db, User

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

auth_bp = Blueprint('auth_bp', __name__)

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