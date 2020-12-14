#!/usr/bin/python3
"""Module documentation """

from sys import argv
from sqlalchemy import create_engine
from model_state import State, Base
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2], argv[3]))

    ses_states = Session(engine)
    for state in ses_states.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    ses_states.close()
