from sqlalchemy import Column, Integer, Float, String, DateTime, Boolean
from sqlalchemy.dialects import postgresql
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Sample(db.Model):
    __tablename__='example'
    __bind_key__ ='sample'
    id = Column(Integer,primary_key=True)
    foo = Column(String,nullable=False,index=True)
    bar = Column(postgresql.ARRAY(String))
