#!/user/bin/python3
"""List all state object s from database hbtn_0e_6_usa"""

import sys
from model_state import State
from model_state import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create SQLAlchemy engine using MySQL credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1],
                                   sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Create a session object
    session = Session()

    # Retrieve all states and pring IDs and names
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))

    # Close session
    session.close()
