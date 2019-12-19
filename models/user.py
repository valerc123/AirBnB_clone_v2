#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    __table__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128),nullbale=False)
    first_name = Column()
    last_name = Column()
