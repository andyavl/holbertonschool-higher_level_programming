#!/usr/bin/python3
"""
Flask authentication example with both Basic Auth and JWT.

This application demonstrates:
- Basic Authentication using Flask-HTTPAuth.
- JWT-based authentication using Flask-JWT-Extended.
- Role-based access control for protected endpoints.
- Error handling for various JWT-related issues.
"""

from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    create_access_token,
    get_jwt_identity
)

app = Flask(__name__)
auth = HTTPBasicAuth()

# Configuration for JWT
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)

# In-memory user store
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    },
}


@auth.verify_password
def verify_password(username, password):
    """
    Verifies username and password for Basic Authentication.

    Args:
        username (str): The username provided by the client.
        password (str): The password provided by the client.

    Returns:
        dict or None: The user object if authentication succeeds;
        otherwise None.
    """
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return user
    return None


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """
    Basic Auth-protected endpoint.

    Returns:
        str: Success message if authentication passes.
    """
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    """
    Authenticates user and issues a JWT token.

    Expects:
        JSON with 'username' and 'password'.

    Returns:
        JSON: Access token if authentication succeeds; error message otherwise.
    """
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username or not password:
        return jsonify({"message": "Missing username or password"}), 400

    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        access_token = create_access_token(
            identity={'username': username, 'role': user['role']})
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Bad username or password"}), 401


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """
    JWT-protected endpoint.

    Returns:
        str: Success message if a valid JWT is provided.
    """
    return "JWT Auth: Access Granted"


@app.route('/admin-only')
@jwt_required()
def admin_only():
    """
    JWT-protected endpoint restricted to admin users.

    Returns:
        str: Admin access confirmation or an error message if access is denied.
    """
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Handles missing or invalid JWT token.
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Handles invalid token errors.
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """
    Handles expired token errors.
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """
    Handles revoked token errors.
    """
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """
    Handles fresh token requirement errors.
    """
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run()
