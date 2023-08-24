#!/usr/bin/python3
"""Print the first State objectfrom the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create the SQLAlchemy engine using MySQL credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3],
                           pool_pre_ping=True)

    # Create a sssion factory and object
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve the first state and print its name and id
    state = session.query(State).order_by(State.id).first()
    if state is None:
        print("Nothing")
    else:
        print("{}: {}."format(state.id, state.name))
