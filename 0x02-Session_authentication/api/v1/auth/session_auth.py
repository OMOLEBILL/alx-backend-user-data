#!/usr/bin/env python3
"""This module extends the auth module"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User


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
        if user_id is None and not isinstance(user_id, str):
            return None
        sessionId = str(uuid.uuid4())
        self.user_id_by_session_id[sessionId] = user_id
        return sessionId

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """We return a user Id based on the session ID
        args:
            session_id : the session id linked to te user id
        returns:
            str: user_id associated with the session_id
        """
        if session_id is None and not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """we return a user based on the sesion cookie
            args:
                request: localproxy
            returns:
                a user based on the cookie
        """
        sesionid = self.session_cookie(request)
        userid = self.user_id_for_session_id(sesionid)
        return User.get(userid)
