# -*- coding: utf-8 -*-
__Author__ = "Amir Mohammad"



# python imports
from sqlalchemy import Column, Integer, String

# project imports
from base import Base



class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    category = Column(String(50), unique=True)
    name = Column(String(50))
    property = Column(String(100))
    number = Column(Integer)
