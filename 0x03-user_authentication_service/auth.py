#!/usr/bin/env python3
"""We hash a given password"""
from bcrypt import hashpw, gensalt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """We hash a password"""
    salt = gensalt()
    return hashpw(password.encode(), salt)


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
