#!/usr/bin/python3
""" review.py """
from models.base.models import BaseModel


class Review(BaseModel):
    """ Review class """

    place_id = ""
    user_id = ""
    text = ""
