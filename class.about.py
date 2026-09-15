'''
CLASS ABOUT
1 - What is class?
2 - ordinary vs static properties
3 - special methods
'''

from urllib import response


print("======= what is class =========")
# class - blueprint for object creation
# structure > state constructor method


class Person:
    # state
    message = "static state property!"
    name = "Goga"
    age = 30

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def introduce(self):
        print(f"{self.name} says: How do you do!")

    def say_age(self):
        print(f"{self.name} is {self.age} years old.")

    @classmethod
    def explain(cls):
        print("static method property executed!")


person1 = Person("Alisher", 25)
person2 = Person("Murod", 30)

# ordinary state
print("person1 name:", person1.name)
print("person2 name:", person2.name)

# ordinary method
person1.introduce()
person1.say_age()
person2.introduce()
person2.say_age()

print("======= ordinary properties va methods =========")
# static state
new_message = Person.message
print("new_message:", new_message)

# static method
Person.explain()

print("======= special / magic methods =========")
# Python's most common special methods are below:
# __init__() __new__() __str__() __call__() __getitem__() __eq__() __len__() ...

class Car():
    # state
    description = "This class makes cars"

    # constructor
    def __new__(cls, *args):
        print("* __new__*")
        return super().__new__(cls)

    def __init__(self, name, year):
        self.name = name
        self.year = year

    # constructor
    def start_engine(self):
        print(f"{self.name} engine started!")

    def stop_engine(self):
        print(f"{self.name} engine stopped!")

    def __call__(self):
        print("Object called as a function!")
        return True

my_car = Car("Porsche", 2026)
my_car.start_engine()
my_car.stop_engine()

print("----------------------------")
your_car = Car("BMW", 2025)
print(your_car)
your_car() # callable object
print("response:", response)