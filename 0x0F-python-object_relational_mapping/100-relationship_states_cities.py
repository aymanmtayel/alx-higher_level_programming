#!/usr/bin/python3
"""script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City


if __name__ == "__main__":
    URL = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(URL.format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()
