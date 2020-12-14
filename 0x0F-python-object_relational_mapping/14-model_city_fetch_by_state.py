#!/usr/bin/python3
""" lists all State objects from the database """
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sys import argv
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2], argv[3]))

    session = Session(engine)
    cities = session.query(State, City).filter(City.state_id == State.id)\
        .order_by(City.id).all()
    for state, city in cities:
        print("{:s}: ({:d}) {:s}".format(state.name, city.id, city.name))
    session.close()
