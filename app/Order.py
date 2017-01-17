# -*- coding: utf-8 -*-
__Author__ = "Amir Mohammad"

# python imports

# project imports
from models.base import session
from models import Item


def validate_order():
    for row in session.query(Item, Item.name).all():
        print(row.Item, row.name)
        # if != null :return 1


class Order:
    def __init__(self):
        pass

    def create_order(self):
        is_validate = validate_order()

        if is_validate:
            #delete in database sqlalchemy
            pass

    def cancel_order(self):
        is_validate = validate_order()
        if is_validate == 0:
            print "Your Order is not valid , check your item."



'''
QUERY :

cookies = session.query(Cookie).all()
for cookie in session.query(Cookie):
    print cookie

cookies = session.query(Cookie).first()

'''
