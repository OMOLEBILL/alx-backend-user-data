#!/usr/bin/env python3
"""We hash a given password"""
from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> bytes:
    """We hash a password"""
    salt = gensalt()
    return hashpw(password.encode(), salt)
