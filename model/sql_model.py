from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime, Integer
import datetime

BASE = declarative_base()

class Todo(BASE):
  __tablename__: str = 'todos'
  _id = Column(Integer, primary_key=True, autoincrement=True)
  todo = Column(String)
  timestamp = Column(DateTime, )