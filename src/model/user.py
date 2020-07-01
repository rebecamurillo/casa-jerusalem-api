from sqlalchemy import Column, String, Integer, DateTime
from .base import Base
import datetime

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    name = Column(String)
    lastname = Column(String)
    update_date = Column(DateTime,default=datetime.datetime.now,onupdate=datetime.datetime.now)
    creation_date = Column(DateTime,default=datetime.datetime.now)

    def __init__(self,email,name,lastname):
        self.email = email
        self.name = name
        self.lastname = lastname
        