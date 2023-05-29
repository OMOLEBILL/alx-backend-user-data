#!/usr/bin/env python3
"""This classes implement the basic authenication"""
import binascii
from api.v1.auth.auth import Auth
import base64
from typing import Tuple, TypeVar
from models.user import User


class BasicAuth(Auth, User):
    """This class extends methods from the auth class"""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """We return part of the header to be encoded"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        strlist = authorization_header.split(' ')
        if len(strlist) == 1:
            return None
        if strlist[0] != "Basic":
            return None
        else:
            return strlist[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """We decode the base64 str into a utf-8"""
        if base64_authorization_header is None or \
                not isinstance(base64_authorization_header, str):
            return None
        try:
            strb = base64.b64decode(base64_authorization_header)
        except (TypeError, binascii.Error):
            return None
        return strb.decode('utf-8')

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """We extract the email from the decoded string"""
        if decoded_base64_authorization_header is None or \
                not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        strlist = decoded_base64_authorization_header.split(':')
        if len(strlist) == 1:
            return (None, None)
        else:
            return (strlist[0], strlist[1])

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """We retrive the user"""
        if user_email is None or not isinstance(user_email, str) or\
           user_pwd is None or not isinstance(user_pwd, str):
            return None
        user = User()
        if user.count() == 0:
            return None
        namelist = user.search({"email": user_email})
        if len(namelist) == 0:
            return None
        else:
            instance = namelist[0]
        if instance.is_valid_password(user_pwd):
            return instance
        else:
            return None
