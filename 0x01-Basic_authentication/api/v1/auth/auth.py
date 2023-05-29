#!/usr/bin/env python3
"""This is a basic authenication module """
from flask import request
from typing import List, TypeVar


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
        if path in excluded_paths:
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