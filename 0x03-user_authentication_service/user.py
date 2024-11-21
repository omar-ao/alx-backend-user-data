#!/usr/bin/env python3
"""
Module for defining the User model for a database table 'users'.
This module adheres to SQLAlchemy ORM and includes all necessary
documentation, type annotations, and stylistic requirements.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    User model class for the 'users' table.
    Defines the structure of the table and its attributes.
    """
    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True)
    email: str = Column(String, nullable=False)
    hashed_password: str = Column(String, nullable=False)
    session_id: str = Column(String, nullable=True)
    reset_token: str = Column(String, nullable=True)
