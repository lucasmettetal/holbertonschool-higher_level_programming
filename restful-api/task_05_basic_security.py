#!/usr/bin/python3
"""
Flask API with Basic Authentication and JWT Token-based Authentication
with Role-based Access Control
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required,
    get_jwt_identity, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Configuration
app.config['JWT_SECRET_KEY'] = 'your-secret-key-change-this-in-production'

# Initialize extensions
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# User data storage
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
    }
}


# Basic Authentication Functions
@auth.verify_password
def verify_password(username, password):
    """Verify username and password for Basic Authentication"""
    if username in users and check_password_hash(
        users[username]['password'], password
    ):
        return username
    return None


@auth.error_handler
def auth_error(status):
    """Custom error handler for Basic Authentication"""
    return jsonify({"error": "Unauthorized access"}), 401


# JWT Error Handlers
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing or invalid token"""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid token"""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """Handle expired token"""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """Handle revoked token"""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """Handle need for fresh token"""
    return jsonify({"error": "Fresh token required"}), 401


# Routes

@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """Protected route using Basic Authentication"""
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    """Login endpoint that returns JWT token"""
    data = request.get_json()

    if not data:
        return jsonify({"error": "Missing JSON data"}), 400

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    # Verify credentials
    if username in users and check_password_hash(
        users[username]['password'], password
    ):
        # Create JWT token with user role in additional claims
        additional_claims = {"role": users[username]['role']}
        access_token = create_access_token(
            identity=username,
            additional_claims=additional_claims
        )
        return jsonify(access_token=access_token), 200

    return jsonify({"error": "Invalid credentials"}), 401


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """Protected route using JWT Authentication"""
    return "JWT Auth: Access Granted"


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """Protected route accessible only by admin role"""
    # Get the current user's identity and claims
    current_user = get_jwt_identity()
    claims = get_jwt()

    # Check if user has admin role
    if claims.get('role') != 'admin':
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
