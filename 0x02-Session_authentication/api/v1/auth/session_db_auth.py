#!/usr/bin/env python3
"""We create a file storage as opposed to memory"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """We extend the SessionExpAuth class"""
    def create_session(self, user_id=None):
        """We overload the create_session"""
        if user_id:
            sessionid = super().create_session(user_id)
            if sessionid:
                user = UserSession(user_id=user_id, session_id=sessionid)
                user.save()
                return sessionid
            return None
        return None
    
    def user_id_for_session_id(self, session_id=None):
        """ We overload the user_id_for_session"""
        
            
    
