#!/usr/bin/env python3
"""This classes implement the basic authenication"""
import binascii
from api.v1.auth.auth import Auth
import base64
from typing import Tuple


class BasicAuth(Auth):
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
