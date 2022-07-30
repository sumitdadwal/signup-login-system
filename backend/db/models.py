from sqlite3 import Timestamp
from .database import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    password = Column(String)
