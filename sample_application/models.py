from sqlalchemy import Column, Integer, Float, String, DateTime, Boolean
from sqlalchemy.dialects import postgresql
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Sample(db.Model):
    '''Sample ORM model. We expect __bind_key__ to be defined'''
    __tablename__ = 'example'
#    __bind_key__ = 'sample'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(String(60), unique=True, nullable=False)
    password_hash = db.Column(String(60), nullable=False)
