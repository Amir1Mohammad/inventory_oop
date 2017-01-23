# -*- coding: utf-8 -*-
__Author__ = "Amir Mohammad & Sepehr"

# python import :
from sqlalchemy.orm import session, query
# project import :
from models import Item
from models.base import session
from app.models.base import Inventory

def notification():
    import Report_Manager


def get_number():
    counter = 0
    for my_id in session.query(Item).filter().all():
        counter += my_id.number
    # print "------", counter
    return counter
# get_number()


def get_id(category, name, property):
    for my_id in session.query(Item).filter(Item.category == category,
                                            Item.name == name, Item.property == property).all():
        # print my_id.id
        return my_id.id


# get_id("Car","Pride","Saba")

def get_capacity():
    for _item in session.query(Inventory).filter():
        # print "------>", _item.Capacity
        return _item.Capacity
# get_capacity()


class LogFile:
    def __init__(self):
        pass

    def log_all(self):
        for _item in session.query(Item).all():
            print "------>", _item.id, _item.category, _item.name, _item.property, _item.number

    def log_category(self, category, name, property):

        for _item in session.query(Item).filter(Item.category == category, Item.name == name,
                                                Item.property == property).all():
            print "------>", _item.id, _item.category, _item.name, _item.property, _item.number

    def deficiency(self, notif):

        for _item in session.query(Item).filter(Item.number <= 1):
            # the print font is not default
            print '\033[1m', _item.id, _item.category, _item.name, _item.property, _item.number
            if notif:
                notification()
            else:
                None


log_obj = LogFile()
# log_obj.log_all()
# log_obj.log_category("Digital","Mobile","samsung")
# log_obj.deficiency(notif=False)
