"""
TASK 1
Write a class to represent a Cash Register.
You class should keep the state of price total and purchased items
Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.
"""

class CashRegister:

    def __init__(self):
        self.total_items = {'chicken nuggets': '2.30'}, \
                           {'chips': '1.00'}, \
                           {'burger': '2.20'}
        self.total_price = 0
        self.item_count = 0

    def add_item(self, item, price):
        self.total_items[item] = price
        return item

    def remove_item(self, item):
        self.total_items.pop(item)

    def apply_discount(self,dicount):
        self.discount = (percentage_discount/100) * discount
        self.total_price = self.total_price - self.discount

    def get_total(self):
        return self.total_price

    def show_items(self):
        return self.total_items

    def reset_register(self):
        self.items = 0
        self.item_count = 0
        self.total_price = 0
#Example code run
checkout = CashRegister()
checkout.add_item('raisins', 2.15)
checkout.add_item('water', 1.00)
checkout.add_item('mangos', 0.70)
checkout.add_item('peas', 0.50)
checkout.get_total()
checkout.apply_discount(60)
checkout.remove_item('water')
checkout.show_items()


"""
TASK 2
Write a base class to represent a student. Below is a starter code. 
Feel free to add any more new features to your class. 
As a minimum a student has a name and age and a unique ID.
Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student. 
"""


class Student:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()

class specialised_subject (student):

   def __init_self,(spec_name):
    self.spec_name = spec_name
    print('specialisation'+str(spec_name))



