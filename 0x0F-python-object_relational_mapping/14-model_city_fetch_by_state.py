#!/usr/bin/python3
"""script 14-model_city_fetch_by_state.py that prints all City objects
from the database hbtn_0e_14_usa"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    URL = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(URL.format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))
    session.close()
