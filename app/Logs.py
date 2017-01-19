# -*- coding: utf-8 -*-
__Author__ = "Amir Mohammad"

# python import :
from sqlalchemy.orm import session, query
# project import :
from models import Item
from models.base import session


def notification():
    import pygame


def get_id(category, name, property):
    for my_id in session.query(Item).filter(Item.category == category, Item.name == name, Item.property == property).all():
        print my_id.id
        return my_id.id

get_id("Car", "Pride", "Saba")


class LogFile:
    def __init__(self):
        pass

    def log_all(self):
        for instance in session.query(Item).order_by(Item.id):
            print(instance.id, instance.category, instance.name, instance.property)

    def log_category(self, category, name, property):
        pass

    def deficiency(self, category, name, property):
        pass




log_obj = LogFile()
# log_obj.log_all()
