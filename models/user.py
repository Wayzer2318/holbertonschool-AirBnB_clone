#!/usr/bin/python3
""" user data model """
from models.base_model import BaseModel


class User(BaseModel):
    """ user data class """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
