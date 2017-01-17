# -*- coding: utf-8 -*-
__Author__ = "Amir Mohammad"

# python import :
from sqlalchemy.orm import session
# project import :
from models import Item
from models.base import session


class DoItem:
    def __init__(self):
        self.id = 10
        self.category = ""
        self.name = ""
        self.property = ""

    def add_item(self, id, category, name, property):
        new_item = Item(id, category, name, property)
        session.add(new_item)
        session.commit()
        print "add_item feature completed"

    def edit_item(self):
        print "edit_item feature completed"
        pass

    def delete_item(self, id):
        print "delete_item feature completed"
        pass


obj = DoItem()
obj.add_item(id=10,category="Digital", name="TV", property="40inch")
