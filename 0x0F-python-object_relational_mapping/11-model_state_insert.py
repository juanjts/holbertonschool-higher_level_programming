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

    add_state = State(name='Louisiana')
    session.add(add_state)
    session.commit()
    print(add_state.id)
    session.close()
