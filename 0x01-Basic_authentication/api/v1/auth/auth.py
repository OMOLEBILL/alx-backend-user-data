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
        return False

    def authorization_header(self, request=None) -> str:
        """We create an authorization error
        args:
            request : the request to create a header
        returns:
            the authorized header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """We create a user """
        return None
