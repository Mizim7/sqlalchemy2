from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///mars_explorer.db', echo=True)

SqlAlchemyBase = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()
