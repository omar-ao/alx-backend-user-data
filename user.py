#!/usr/bin/env python3
"""User Module"""
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    """
    User class
    """
    __tablename__ = 'users'  # Specify the table name

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False)
    hashed_password = db.Column(db.String, nullable=False)
    session_id = db.Column(db.String, nullable=True)
    reset_token = db.Column(db.String, nullable=True)

    def __repr__(self):
        return f"<User id={self.id} email={self.email}>"
