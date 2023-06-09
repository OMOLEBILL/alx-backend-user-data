#!/usr/bin/env python3
"""We implement a simple reduction"""
import re
from typing import List
import logging
import mysql.connector
from os import getenv


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
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
        message = re.sub(f'{i}=.*?{separator}',
                         f'{i}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.args = fields

    def format(self, record: logging.LogRecord) -> str:
        """ we implement a mini format method
            arg:
                record : a record from the logging.LogRecord
            return:
                a formatted string
        """
        return filter_datum(self.args, self.REDACTION, super().format(record),
                            self.SEPARATOR)


def get_logger() -> logging.Logger:
    """we implement a logger "user_data" and only log up to logging.INFO level.
        It should not propagate messages to other loggers. It should have a
        StreamHandler with RedactingFormatter as formatter
    """
    Logger = logging.getLogger("user_data")
    Logger.setLevel(logging.INFO)
    Logger.propagate = False
    formatter = RedactingFormatter(list(PII_FIELDS))
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    Logger.addHandler(handler)
    return Logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """we use the Use os module to obtain credentials from the environment"""
    name = getenv("PERSONAL_DATA_DB_USERNAME")
    password = getenv("PERSONAL_DATA_DB_PASSWORD")
    host = getenv("PERSONAL_DATA_DB_HOST")
    database = getenv("PERSONAL_DATA_DB_NAME")
    return mysql.connector.connect(user=name, host=host,
                                   database=database, password=password)


def main():
    """The engine of this module"""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    logger = get_logger()
    for item in cursor:
        mess = f"name={item[0]}; email={item[1]}; phone={item[2]}; " +\
            f"ssn={item[3]}; password={item[4]};ip={item[5]}; " +\
            f"last_login={item[6]}; user_agent={item[7]};"
        mess = filter_datum(list(PII_FIELDS), "***", mess, "; ")
        logger.info(mess)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
