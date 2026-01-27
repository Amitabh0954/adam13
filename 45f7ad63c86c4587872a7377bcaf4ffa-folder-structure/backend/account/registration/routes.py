# Epic Title: User Account Management

from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from models import User  # Assuming models.py contains a User model
from database import db_session

registration_bp = Blueprint('registration_bp', __name__)

@registration_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    # Email must be unique
    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'Email already in use'}), 400

    # Password must meet security criteria
    if not is_password_secure(password):
        return jsonify({'message': 'Password does not meet security criteria'}), 400

    new_user = User(email=email, password=generate_password_hash(password))
    db_session.add(new_user)
    db_session.commit()
    
    return jsonify({'message': 'User registered successfully'}), 201

def is_password_secure(password: str) -> bool:
    # Implement your password security criteria here
    if len(password) < 8:
        return False
    return True