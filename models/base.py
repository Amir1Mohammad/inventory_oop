# -*- coding: utf-8 -*-
__Author__ = "Amir Mohammad"


# Python imports
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('sqlite:///database.db', echo=True)
session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=True,
                                         bind=engine))
Base = declarative_base()
Base.query = session.query_property()
def init_db():
    Base.metadata.create_all(bind=engine)

class Inventory(Base):
    __tablename__ = 'inventory'

    Capacity = Column(Integer, primary_key=True)

