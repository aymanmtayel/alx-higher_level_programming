#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """create engine and connet to database"""
    URL = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine_create = create_engine(URL.format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine_create)
    session = Session()
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
