#!/usr/bin/env python3
"""We implement a simple reduction"""
import re


def filter_datum(fields: list, reduction: str,
                 message: str, separotor: str) -> str:
    """We reduct the messages with the given reduction
       args:
            fields : list of strings representing all fields to obfuscate
            redaction: a string representing by what the field will be
            obfuscated
            message: a string representing the log line
            separator: a string representing by which character is separating
            all fields in the log line (message)
        returns:
            it returns the obfuscated message
    """
    for i in fields:
        message = re.sub(
            r'\{}{}\=(.*?)\{}'.format(separotor, i, separotor),
            r'{}{}={}{}'.format(separotor, i, reduction, separotor), message
        )
    return message
