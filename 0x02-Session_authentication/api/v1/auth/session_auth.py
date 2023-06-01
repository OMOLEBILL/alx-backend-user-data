#!/usr/bin/env python3
"""This module extends the auth module"""
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """This class inherits from the Auth class"""

    def __init__(self) -> None:
        """We intialiaze the instance of this class"""
        super().__init__()
