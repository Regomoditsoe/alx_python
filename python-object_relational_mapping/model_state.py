#!/user/bin/python3
"""Define a state and an instance Base = declarative_base()"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """Representing a state for MySQL database.
    __tablename__: Name of MySQL table to store states.
    id (sqlalchemy.integer): State's id.
    name (sqlalchemy.string): Name of the state."""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
