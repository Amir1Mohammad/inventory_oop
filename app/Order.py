# -*- coding: utf-8 -*-
__Author__ = "Amir Mohammad"

# python imports

# project imports
from models.base import session
from models import Item
from Logs import get_id


def item_number(category,name,property):
    for item_ in session.query(Item).filter(Item.category == category, Item.name == name,
                                            Item.property == property).all():
        return item_.number

class Order:
    def __init__(self):
        pass

    def create_order(self,category,name,property,number):
        items_number = item_number (category,name,property)
        if items_number <  number:
            print "This Order is not Valid . Check your inventory again ."
            self.cancel_order()
        else:
            o_id = get_id(category, name, property)
            u = session.query(Item).get(o_id)
            print u.number
            u.number = u.number - number
            session.commit()
            print "Created Order Successfully !"


    def cancel_order(self):
        print "Ordered Canceled Successfully !"


order_obj = Order()
# order_obj.create_order("Digital","Mobile","samsung",2)
# order_obj.create_order("Car","Pride","hachbach",1)
