#!/usr/bin/env python3
"""We hash pasword with the use of bcrypt"""
import bcrypt


def hash_password(password: str) -> bytes:
    """We hash and salt the given password
        args:
            password: password to be hashed
        returns
            a salted and hashed password
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """We validate the given password
       args:
            hashed_password : the password to compare with
            password: te string password
        returns a boolen
    """
    if bcrypt.checkpw(password.encode("utf-8"), hashed_password):
        return True
    return False
