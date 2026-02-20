#!/usr/bin/python3
"""
A simple API using Python with Flask
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user storage
users = {}


@app.route('/')
def home():
    """
    Root endpoint - returns welcome message
    """
    return "Welcome to the Flask API!"


@app.route('/data')
def get_users():
    """
    Returns list of all usernames in the API
    """
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """
    Returns OK status
    """
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """
    Returns user data for the specified username
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Add a new user to the API
    Expects JSON data with username, name, age, and city
    """
    # Check if request contains valid JSON
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()

    # Check if username is provided
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Check if username already exists
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Add the new user
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    app.run(debug=True)
