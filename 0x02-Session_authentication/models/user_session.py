#!/usr/bin/env python3
"""We store the session IDS in a file instead"""
from  models.base import Base


class UserSession(Base):
    """we STORE the user session"""
    def __init__(self, *args: list, **kwargs: dict):
        """We intailiaze the instance methods"""
        super().__init__(*args, **kwargs)
        if kwargs.get("user_id"):
            self.user_id = kwargs.get("user_id")
        if kwargs.get("session_id"):
            self.session_id = kwargs.get("session_id")
    
