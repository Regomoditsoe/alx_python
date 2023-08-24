#!/user/bin/python3
"""List all State objects containing `a` from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create SQLAlchemy enging using MySQL credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                            pool_pre_ping=True)

    # Create a session factory and object
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve states with letter 'a' and print names and id
    for state in session.query(State).order_by(State.id):
        if "a" in state.name.lower():
            print("{}: {}".format(state.id, state.name))

