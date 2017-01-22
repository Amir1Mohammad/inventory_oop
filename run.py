# -*- coding: utf-8 -*-
__Author__ = "Amir Mohammad"
#pyhton imports :
try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q

#projcet imports :

from app.item import Category,Name,DoItem
from app.Logs import LogFile
from app.Order import Order



# Request queue priority
# q = Q.PriorityQueue()
# q.put((10, 'ten'))
# q.put((1, 'one'))
# q.put((5, 'five'))
# while not q.empty():
#     print q.get(),


def run():
    pass
