#!/usr/bin/env python3
""" Module for the session authentification views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from os import getenv
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def userLogin():
    """ POST /auth_session/login
    request.form
      - email
      - password
    Return:
      - User object JSON represented
      - 400 if can't create the new User
    """
    from api.v1.app import auth
    email = request.form.get("email")
    pasword = request.form.get("password")
    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400
    if pasword is None or pasword == "":
        return jsonify({"error": "password missing"}), 400
    instancelist = User.search({"email": email})
    if len(instancelist) == 0:
        return jsonify({"error": "no user found for this email"}), 404
    for instance in instancelist:
        if not instance.is_valid_password(pasword):
            return jsonify({"error": "wrong password"}), 401
        sessionId = auth.create_session(instance.id)
        res = jsonify(instance.to_json())
        res.set_cookie(getenv("SESSION_NAME"), sessionId)
        return res
