# -*- coding: utf-8 -*-
__Author__ = "Amir Mohammad"

# python import :
from sqlalchemy.orm import session

# project import :
from models import Item
from models.base import session, init_db

init_db()


def is_category(category):
    category_list = session.query(Item.category).all()
    print category_list
    if (u'amir',) in category_list:
        print "Yes , There is"
        return True


is_category((u'amir',))


# in bi manie , chon khodesh add mikone .
def add_category(category):
    pass


class DoItem:
    def __init__(self):
        pass

    def add_item(self, id, category, name, property, number):
        new_item = Item(id=id, category=category, name=name, property=property, number=number)
        session.add(new_item)
        session.commit()
        print "add_item feature completed"

    def edit_item(self, id):
        # session.commit()
        print "edit_item feature completed"

    def delete_item(self, id):
        user = Item.query.get(id)
        session.delete(user)
        session.commit()
        print "delete_item feature completed"


DoItem_obj = DoItem()
DoItem_obj.add_item(30,"Fruit", "Pride", "Saba", 2)
DoItem_obj.delete_item(30)
