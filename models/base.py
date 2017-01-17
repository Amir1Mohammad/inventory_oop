# -*- coding: utf-8 -*-
__Author__ = "Amir Mohammad"


# Python imports
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///database.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
Base.metadata.create_all(bind=engine)


class Inventory(Base):
    __tablename__ = 'inventory'

    Capacity = Column(Integer, primary_key=True)

