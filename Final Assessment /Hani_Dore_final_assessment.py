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

(B)
B.1
Design a child class called Dog, which inherits from the Animal class.
This class should have exactly the same attributes as its parent class,
as well as additional ones called:
pet_id and breed (any other attributes are welcome - they are optional).
You child class Dog should also have a static method called sound(), which
would give us the sound of the animal ('Grr', 'Bark', whatever you want)

B.2
Design a child class called Cat, which inherits from the Animal class.
This class should have exactly the same attributes as its parent class,
as well as additional ones called:
pet_id and breed (any other attributes are welcome - they are optional).
You child class Dog should also have a static method called sound(), which
would give us the sound of the animal ('Meow', 'Purr', whatever you want)

(C)
Design an independent class called PetOwner. It is a small class, which should
have the __init__ method only accepting the 'name of an owner' and 'pet's id'.

SEE THE STARTER CODE BELOW

"""

from datetime import date

class Animal
    def__innit__(self, name, dob, colour, owner):
    self.name = name
    self.dob = dob
    self.colour = colour
    self.owner = owner

    def get_age (self, dob):
        today = date.today()
        date_obj = datetime(dob, '%d%m%y')

        return {'years': int(date.today().year - year), 'months': int(date.today().month - month )}


class Dog(Animal):
    def __innit__(self, name, colour, dob,  owner, pet_id, breed):
        super().__init__(name, dob, colour, owner)
        self.breed = breed
        self.pet_id =  pet_id

        @staticmethod
        def sound():
            sound = 'Grr'
            return sound

class Cat (Animal):
    def __innit__(self, name, colour,dob, owner, pet_id, breed ):
        super().__init__(name, dob, colour, owner)
        self.breed = breed
        self.pet_id = pet_id

        @staticmethod
        def sound()
            sound = 'purr'
            return sound

class PetOwner:
    def__innit__(self, pet_id, owner):
    self.pet_id = pet_id
    self.owner = owner

    """
    TASK 2
    
    We are going to utilize classes that we created as part of TASK 1. 
    
    Let's imagine that we are a local vet clinic and given the input below, we 
    need to add all pets to our register (register is just a dict). 
    
    Please write a function, which parses given input and initializes a class for
    each animal, as well as its owner and adds it to the register by id. 
    
    EXAMPLE OUTPUT:
    
    {
     10025: <__main__.Dog object at 0x0829DFB8>,
     10026: <__main__.Cat object at 0x082B4D90>,
     10042: <__main__.Dog object at 0x082B4130>,
     10053: <__main__.Dog object at 0x082B47F0>,
     10058: <__main__.Cat object at 0x07C80B50>
     }

     Each key is a pet id and each value is a newly initialized  Dog or Cat class. 
     Note that within each Dog and Cat class the variable "self.owner" is also 
     a class PetOwner with all relevant attributes.
    
    SEE THE STARTER CODE BELOW

    """

    pet_info = [
        {'breed': 'German Shepherd',
         'colour': 'brown',
         'dob': '2021/09/21',
         'pet_id': 10025,
         'name': 'Lola',
         'owner': 'Maria Smith',
         'type': 'dog'},
        {'breed': 'Blue Russian',
         'colour': 'white',
         'dob': '2010/03/06',
         'pet_id': 10058,
         'name': 'Snowy',
         'owner': 'Malcolm Graham',
         'type': 'cat'},
        {'breed': 'Border Collie',
         'colour': 'beige',
         'dob': '2019/11/18',
         'pet_id': 10042,
         'name': 'Bailey',
         'owner': 'Priya Patel',
         'type': 'dog'},
        {'breed': 'Pug',
         'colour': 'black',
         'dob': '2021/10/16',
         'pet_id': 10053,
         'name': 'Ziggy',
         'owner': 'Mohamed Moussa',
         'type': 'dog'},
        {'breed': 'Sphynx',
         'colour': 'white',
         'dob': '2015/08/23',
         'pet_id': 10026,
         'name': 'Coco',
         'owner': 'Jennifer Coley',
         'type': 'cat'}
    ]



    def register_pets(data):
        pets = dict()
        return pets

    print(register_pets(pet_info))


"""
TASK 3

Write a function to sum up the digits of a given number.

EXAMPLE:

num = 78
result = 15

num = 333
result = 9

num = 12345
result = 15
===============================

Using recursion = 25 points
Any non recursive solution = 15 points

===============================

Hints for recursive approach:

1) Get the rightmost digit of the number with help of remainder 
‘%’ operator by dividing it with 10

2) Dividing a number by 10 with help of ‘/’ operator and converting it to int
helps you to 'move or iterate' through a number
"""

def total (num):
    return 0
if num == 0
    else int(num % 10) + total(int(num/10))

total (78)
total(333)
total(12345)

"""


TASK 4

CODING TASK

Write a function that takes in a non-empty string and returns its 
run-length encoding.

● For example, the run “AAA” will be “3A”
● The input string can contain special characters, including numbers 
● Long runs(10 or more chars) must be encoded in a split fashion:  
  “AAAAAAAAAAAA” (12 “A” s) → encoded as “9A3A”


Sample Input
string = "AAAAAAAAAAAAABBCCCCDD"

Sample Output
expected = "9A4A2B4C2D"

HINTS: 
● Traverse the input string and count the length of each run. 
As you traverse the string, what would you do when you reach a 
run of length 9 or the end of a run?
● When you reach a run of length 9 or the end of a run, 
store the computed count for the run, as well as its character.
● Make sure that your solution correctly handles the last run in the string. 
"""

def rle_encoding(string):
    pass


string = "AAAAAAAAAAAAABBCCCCDD"
print(rle_encoding(string)) # Expected "9A4A2B4C2D"


