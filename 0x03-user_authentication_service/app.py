#!/usr/bin/env python3
"""We serve the app"""
from flask import (Flask, make_response,
                   jsonify, request, abort)
from os import getenv
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def Home():
    """The place that i would got to"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """We post a user if it doesn't exist"""
    email = request.form.get("email")
    password = request.form.get("password")
    user = None
    if email and password:
        try:
            user = AUTH.register_user(email, password)
        except ValueError:
            return jsonify({"message": "email already registered"}), 400
    return jsonify({"email": f"{user.email}", "message": "user created"})


@app.route("/sessions", methods=['POST'], strict_slashes=False)
def login():
    """We validate the login if sucessful we store it in a cookie"""
    email = request.form.get("email")
    password = request.form.get("password")
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response
    else:
        abort(401)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
