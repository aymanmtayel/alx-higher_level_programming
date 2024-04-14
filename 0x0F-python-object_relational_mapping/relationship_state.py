#!/usr/bin/python3
"""python file that contains the class definition of a State"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """Base class for states table"""
    __tablename__ = 'states'

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
