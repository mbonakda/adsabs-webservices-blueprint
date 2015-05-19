"""
Database models
"""

from sqlalchemy import Column, Integer, Float, String, DateTime, Boolean
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class FavoriteColor(db.Model):
    """
    Sample database model. __bind_key__ should be specified in the case that
    connections to multiple distinct databases are required.
    """
    #__bind_key__ = 'sample_application'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(String(60), unique=True, nullable=False)
    color = db.Column(String(60), nullable=True)
