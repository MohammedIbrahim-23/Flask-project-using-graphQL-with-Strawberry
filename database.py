from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm import declarative_base

# Configure the PostgreSQL database connection
engine = create_engine("postgresql://postgres:#86089070j@localhost/day1?port=5432")
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base(cls=object, name='Base')
Base.query = db_session.query_property()

if engine:
    print("connected")
else:
    print("not connected")

# Initialize the database
def init_db():
    import models
    Base.metadata.create_all(bind=engine)
