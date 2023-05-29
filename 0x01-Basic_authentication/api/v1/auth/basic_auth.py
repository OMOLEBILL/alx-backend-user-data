#!/usr/bin/env python3
"""This classes implement the basic authenication"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """This class extends methods from the auth class"""
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """We return part of the header to be encoded"""
        if authorization_header is None:
            return None
        if type(authorization_header) != str:
            return None
        strlist = authorization_header.split(' ')
        if len(strlist) == 1:
            return None
        if strlist[0] != "Basic":
            return None
        else:
            return strlist[1]
