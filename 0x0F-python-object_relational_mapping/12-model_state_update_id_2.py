#!/usr/bin/python3
"""script that changes the name of a State object from
the database hbtn_0e_6_usa"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    URL = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(URL.format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    old_state = session.query(State).filter_by(id=2).first()
    if old_state:
        old_state.name = "New Mexico"
        session.commit()
