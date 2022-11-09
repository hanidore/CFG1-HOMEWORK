"""
TASK 1
(A)
Design a parent class called Animal

It must have general attributes: name, date of birth, colour, owner's name
Also it must have a method that gives you the age of an animal.

For example, if animal's date of birth is 2021/08/21 and today is
11 January 2021, the when you call get_age()
<name your method whatever you want> method, it should give us the age in
YEAR and MONTH like this: {'years': 0, 'months': 4}



"""
import random


class Animal:

    def __init__(self, name, dob, colour, owner):
        self.name = name
        self.dob = dob
        self.colour = colour
        self.owner = owner


    @staticmethod
    def generate_age():
        age = str(random.randrange(0, 100))
        return age


    def get_age(self,):
      return {'years': int(year), 'months': int(month)}


class Dog(Animal):
    def__init__(self, pet_id, breed ):

    self.breed = breed
    self.pet_id = pet_id