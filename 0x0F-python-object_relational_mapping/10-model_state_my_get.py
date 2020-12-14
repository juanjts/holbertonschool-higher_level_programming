#!/usr/bin/python3
"""Start link class to table in database"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2], argv[3]))

    session = Session(engine)
    ses_state = session.query(State).order_by(State.id).filter(
        State.name == argv[4]).first()
    if ses_state:
        print('{}'.format(ses_state.id))
    else:
        print("Not found")
    session.close()
