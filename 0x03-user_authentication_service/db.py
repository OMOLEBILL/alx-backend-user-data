#!/usr/bin/env python3
"""DB module contains all user details
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from typing import Dict

from user import Base, User


class DB:
    """DB class we implement the database connestion
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """We add a user to the database"""
        instance = User(email=email, hashed_password=hashed_password)
        self._session.add(instance)
        self._session.commit()
        return instance

    def find_user_by(self, **kwargs) -> User:
        """We filter the user database"""
        user = self._session.query(User).filter_by(**kwargs).first()
        if user:
            return user
        raise NoResultFound

    def update_user(self, user_id: int, **kwargs) -> None:
        """We update the user given its id"""
        user = self.find_user_by(id=user_id)
        for arg, value in kwargs.items():
            if hasattr(user, arg):
                setattr(user, arg, value)
            else:
                raise ValueError
        self._session.commit()
