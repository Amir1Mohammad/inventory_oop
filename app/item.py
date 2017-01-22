# -*- coding: utf-8 -*-
__Author__ = "Amir Mohammad"

# python import :
from sqlalchemy.orm import session

# project import :
from models import Item
from models.base import session, init_db

init_db()

class Category:
    def is_new_category(self, category):
        category_list = session.query(Item.category).all()
        if (str(category),) in category_list:
            return False
        else :
            return True

        
    def add_category(self, category):
        if self.is_new_category(category):
            return category

    def edit_category(self, category1, category2):
        if not self.is_new_category(category1):
            cat_list = [category1, category2]
            return cat_list


    def delete_category(self, category):
        if not self.is_new_category(category):
            return category



class Name:
    def is_new_item(self, category, name):
        categ_obj = Category()
        if not categ_obj.is_new_category(category):
            item_list = session.query(Item.name).all()
            if (str(name),) in item_list:
                return False
            else :
                return True

    def add_item(self, category, name):
        if self.is_new_item(category, name):
            return name


    def edit_item(self, category, name1, name2):
        if not self.is_new_name(category, name1):
            name_list = [name1, name2]
            return name_list


    def delete_item(self, category, name):
        if not self.is_new_name(category, name):
            return name




class DoItem:
    def check_category(self, category):
        cat_obj = Category()
        if cat_obj.is_new_category(category):
            return True
        else:
            return False

            
    def check_name(self, category, name):
        nam_obj = Name()
        if nam_obj.is_new_item(category, name):
            return True
        else:
            return False
        
    def add_item(self, id, category, name, property, number):
        new_item = Item(id=id, category = category, name = name, property=property, number=number)
        session.add(new_item)
        session.commit()
    def edit_item(self, id, category, name, property1, property2):
        if (not self.check_category(category)) and (not self.check_name(category, name)):
            ######bayad avaz she
            u = session.query(Item).get(id)
            u.name = name
            session.commit()
            print "edit_item feature completed"
            #############
    def delete_item(self, id):
        if (not self.check_category(category)) and (not self.check_name(category, name)):
            ############
            user = Item.query.get(id)
            session.delete(user)
            session.commit()
            print "delete_item feature completed"
            ################

DoItem_obj = DoItem()

#DoItem_obj.add_item(11,"Mive", "Sib", "Damavand", 20)
#DoItem_obj.add_item(2,"Food", "pizza", "gharch", 50)
# DoItem_obj.add_item(30,"Digital", "Mobile", "samsung", 100)
# DoItem_obj.add_item(40,"Home", "clock", "analog", 1)
# DoItem_obj.edit_item(31,"havapeyma")
# DoItem_obj.delete_item(1)
