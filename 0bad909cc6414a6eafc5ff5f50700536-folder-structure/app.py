# Epic Title: User Account Management

from flask import Flask, request, jsonify
import mysql.connector
from backend.repositories.user_account.user_repository import UserRepository
from backend.services.user_account.user_service import UserService

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data['email']
    password = data['password']

    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="mydatabase"
    )

    user_repository = UserRepository(db_connection)
    user_service = UserService(user_repository)
    result = user_service.register_user(email, password)

    if result:
        return jsonify({'error': result}), 400

    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']

    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="mydatabase"
    )

    user_repository = UserRepository(db_connection)
    user_service = UserService(user_repository)
    result = user_service.authenticate_user(email, password)

    if result:
        return jsonify({'error': result}), 400

    return jsonify({'message': 'Login successful'}), 200

@app.route('/password-reset-request', methods=['POST'])
def password_reset_request():
    data = request.get_json()
    email = data['email']

    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="mydatabase"
    )

    user_repository = UserRepository(db_connection)
    user_service = UserService(user_repository)
    result = user_service.send_password_reset_email(email)

    if result:
        return jsonify({'error': result}), 400

    return jsonify({'message': 'Password reset email sent successfully'}), 200

@app.route('/password-reset', methods=['POST'])
def password_reset():
    data = request.get_json()
    email = data['email']
    token = data['token']
    new_password = data['new_password']

    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="mydatabase"
    )

    user_repository = UserRepository(db_connection)
    user_service = UserService(user_repository)
    result = user_service.reset_password(email, token, new_password)

    if result:
        return jsonify({'error': result}), 400

    return jsonify({'message': 'Password reset successfully'}), 200

@app.route('/update-profile', methods=['PUT'])
def update_profile():
    data = request.get_json()
    email = data['email']
    profile_data = data['profile_data']

    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="mydatabase"
    )

    user_repository = UserRepository(db_connection)
    user_service = UserService(user_repository)
    result = user_service.update_user_profile(email, profile_data)

    if result:
        return jsonify({'error': result}), 400

    return jsonify({'message': 'Profile updated successfully'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)