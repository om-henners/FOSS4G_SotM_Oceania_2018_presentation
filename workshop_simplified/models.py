from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

host = 'host'
port = 'port'
database = 'database'
username = 'username'
password = 'password'

connection = f'postgresql://{username}:{password}@{host}:{port}/{database}'
engine = create_engine(connection) # optionally: verbose=True)


Base = declarative_base()

class VotingCentre(Base):
    __tablename__ = 'voting_centre'
    id = Column(Integer, primary_key=True)
    venue_name = Column(String)
