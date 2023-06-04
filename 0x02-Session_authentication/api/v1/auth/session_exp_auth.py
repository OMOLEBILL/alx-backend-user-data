#!/usr/bin/env python3
"""We extend the session auth class by adding an expiry"""
from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """We create an expiration to a session"""

    def __init__(self):
        """We intialiaze the instances"""
        try:
            self.session_duration = int(getenv("SESSION_DURATION"))
        except TypeError:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """we overload the base class create method"""
        if user_id:
            sessionid = super().create_session(user_id)
            if sessionid:
                self.user_id_by_session_id[sessionid] = {
                    "user_id": user_id,
                    "created_at": datetime.now()
                }
                return sessionid
            return None
        return None

    def user_id_for_session_id(self, session_id=None):
        """We overload the userid for session id"""
        if session_id:
            sessiondict = self.user_id_by_session_id.get(session_id)
            if sessiondict:
                if self.session_duration <= 0:
                    return sessiondict.get("user_id")
                created_at = sessiondict.get("created_at")
                if not created_at:
                    return None
                if datetime.now() > created_at + timedelta(
                        seconds=self.session_duration):
                    return None
                return sessiondict.get("user_id")
            return None
        return None
