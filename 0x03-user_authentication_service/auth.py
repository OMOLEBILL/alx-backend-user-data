#!/usr/bin/env python3
"""We hash a given password"""
from bcrypt import hashpw, gensalt, checkpw
from db import DB
from user import User
from uuid import uuid4
from typing import Any


def _hash_password(password: str) -> bytes:
    """We hash a password"""
    salt = gensalt()
    return hashpw(password.encode(), salt)


def _generate_uuid() -> str:
    """generates a uuid"""
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self) -> None:
        """WE initiliase the class"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """We register a user if it doesn't exist"""
        hashed_password = _hash_password(password)
        user = None
        try:
            user = self._db.find_user_by(email=email)
        except Exception:
            pass
        if user and user.email == email:
            mess = f"User {email} already exists"
            raise ValueError(mess)
        else:
            return self._db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """We check if the email matches the given password"""
        try:
            user = self._db.find_user_by(email=email)
        except Exception:
            return False
        if checkpw(password.encode(), user.hashed_password):
            return True
        return False

    def create_session(self, email: str) -> Any:
        """We create a sessionid from the email"""
        try:
            user = self._db.find_user_by(email=email)
            sessionId = _generate_uuid()
            self._db.update_user(user.id, session_id=sessionId)
        except Exception:
            return None
        return user.session_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """We search for a user by session_id"""
        try:
            user = self._db.find_user_by(session_id=session_id)
            if user.session_id:
                return user
            return None
        except Exception:
            return None

    def destroy_session(self, user_id: int) -> int:
        """We update the seesion_id to None"""
        self._db.update_user(user_id, session_id=None)
        return None

    def get_reset_password_token(self, email: str) -> str:
        """We reset the password token"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                reset_token = _generate_uuid()
                self._db.update_user(user.id, reset_token=reset_token)
                return reset_token
            raise ValueError
        except Exception:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """We update a password"""
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            if user:
                hashedpassword = _hash_password(password)
                self._db.update_user(
                    user.id, hashed_password=hashedpassword, reset_token=None)
                return None
            raise ValueError
        except Exception:
            raise ValueError
