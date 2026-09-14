'''
OBJECTS
1 - What is object?
2 - Iterables objects and RANGE
3 - Dictionary
4 - Error handling system
'''

import array  # package/module
import math  # package
from math import ceil
print("======= what is object =========")
# an abject has state and method properties
# everything in Python is object

print(type('Hello world'))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# Paradigme > Functional Programming & Object Oriented Programming (OOP)
# OOP 4 CONCEPTS > Abstraction, Encapsulation, Inheritance, Polymorphism
result1 = math.ceil(10.5)  # called method of math object
print(result1)

result2 = ceil(14.5)  # called method of math object
print(result2)

print("======= Error Handling system =========")
car_dict = dict(name="BMW", model="X5", year=2020, electric=True)
try:
    print("passed here")
    result = car_dict["origin"]
    print("result:", result)
except Exception as err:
    print("Error:", err)
finally:
    print("Final closing logic")
