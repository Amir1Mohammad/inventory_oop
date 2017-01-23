__author__ = "Amir Mohammad & Sepehr"



from app.item import Category,Name,DoItem
from app.Logs import LogFile
from app.Order import Order
from app.models.base import set_capacity
from time import sleep



# set_capacity(500)
print "Test all feature in the Inventory Framework :)"
DoItem_obj = DoItem()
DoItem_obj.add_item(11,"Mive", "Sib", "Damavand", 20)
DoItem_obj.add_item(10,"Food", "pizza", "chicken", 50)
DoItem_obj.add_item(30,"Digital", "Mobile", "samsung", 100)
DoItem_obj.add_item(40,"Home", "clock", "analog", 1)
print "---------------- ADD DB Feature Tested ----------------!"
DoItem_obj.edit_item("Mive", "Sib", "Damavand", 20,"Mive", "holo", "save", 22)



log_obj = LogFile()
log_obj.log_all()
log_obj.log_category("Digital","Mobile","samsung")
log_obj.deficiency(notif=False)
sleep(1)
print "---------------- logF Feature Tested ----------------!"

order_obj = Order()
order_obj.create_order("Digital","Mobile","samsung",2)
order_obj.create_order("Home", "clock", "analog",1)

log_obj.log_all()

DoItem_obj.delete_item("Mive", "holo")
DoItem_obj.delete_item("Food", "pizza")
DoItem_obj.delete_item("Digital", "Mobile")
DoItem_obj.delete_item("Home", "clock")
#Delete the set capacity
print "---------------- Create Order Feature Tested ----------------"
print "Have Nice Time !"
