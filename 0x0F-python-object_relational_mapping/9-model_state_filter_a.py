#!/usr/bin/python3
"""script that lists all State objects that contain the letter a
from the database hbtn_0e_6_usa"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    URL = "mysql+mysqldb://{}:{}@localhost/{}"
    engine = create_engine(URL.format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    filter_a = State.name.like('%a%')
    states_a = session.query(State).order_by(State.id).filter(filter_a)
    for state in states_a:
        print("{}: {}".format(state.id, state.name))
    session.close
