#!/usr/bin/env python3
"""This is a basic authenication module """
from flask import request
from typing import List, TypeVar
from re import match
from os import getenv


class Auth():
    """This is the basic authenication class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """We check if a route require authenication
        args:
            @path : the route to check
            @excluded_list : the list that do not require authenication
        returns:
            bool
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if not path.endswith('/'):
            path += '/'
        for string in excluded_paths:
            if string.endswith("*"):
                pattern = rf"^{string[:-1]}.*$"
                if match(pattern, path):
                    return False
                else:
                    return True
            elif path in excluded_paths:
                return False
            else:
                return True

    def authorization_header(self, request=None) -> str:
        """We create an authorization error
        args:
            request : the request to create a header
        returns:
            the authorized header
        """
        if request is None:
            return None
        if "Authorization" not in request.headers:
            return None
        else:
            return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """We create a user """
        return None

    def session_cookie(self, request=None):
        """We return a cookie value from a request
            args:
                request : LocalProxy
            returns:
                the session cookie
        """
        if request is None:
            return None
        sessionId = getenv("SESSION_NAME")
        return request.cookies.get(sessionId)
