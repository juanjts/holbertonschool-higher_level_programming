#!/usr/bin/python3
"""Module documentation """

from sys import argv
from sqlalchemy import create_engine
from model_state import State, Base
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2], argv[3]))

    session = Session(engine)
    ses_state = session.query(State).order_by(State.id).filter(
        State.name.contains('a'))
    for states in ses_state:
        print('{}: {}'.format(states.id, states.name))
    session.close()
