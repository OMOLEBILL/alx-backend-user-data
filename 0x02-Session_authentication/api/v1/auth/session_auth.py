#!/usr/bin/env python3
"""This module extends the auth module"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """This class inherits from the Auth class"""
    user_id_by_session_id = {}

    def __init__(self) -> None:
        """We intialiaze the instance of this class"""
        super().__init__()

    def create_session(self, user_id: str = None) -> str:
        """We create a session Id for the user id
        args:
            user_id : User id to generate a seesion id to
        returns:
            str: the sesion id
        """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        sessionId = str(uuid.uuid4())
        self.user_id_by_session_id[sessionId] = user_id
        return sessionId
