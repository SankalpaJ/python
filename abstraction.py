''' Rule 1: We can create an object for empty abstract cls...
    Rule 2: If abst cls contains abst method then object for that 
             abst cls can't be created & abst method can't be invoked...
    Rule 3: If abst cls contains only concrete method, then obj can be created
             & concrete method(which method as some implentation) can be invoked...
    Rule 4: If cls z derived from abst cls & not given body for all abst methods
              in child cls then child cls obj can't created...
'''

# Rule 1:
from abc import ABC, abstractclassmethod
class Animal1(ABC):
    pass
a1 = Animal1()     # executed

# Rule 2:
class Animal2(ABC):
    @abstractclassmethod
    def eat(self):
        pass           # Error
# a2 = Animal()

# Rule 3:
class Animal3(ABC):
    def eat(self):
        print("Inside eat")
a3 = Animal3()
a3.eat()                  # Inside eat

# Rule 4:
class Animal4():
    @abstractclassmethod
    def eat(self):
        pass
    @abstractclassmethod
    def sleep(self):
        pass
class Child(Animal4):
    def eat(self):
        print('Inside eat')
# c = Child()         Not allowed

# kapp prlm--------------------
from abc import ABC, abstractmethod
import math
# Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
# Rectangle Class inheriting from Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)
# Circle Class inheriting from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return round(math.pi * self.radius ** 2, 2)
    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)
# Taking input from user
length = float(input())
width = float(input())
radius = float(input())
# Creating instances
rectangle = Rectangle(length, width)
circle = Circle(radius)
# Displaying area and perimeter
print(f"Rectangle Area: {rectangle.area()}")
print(f"Rectangle Perimeter: {rectangle.perimeter()}")
print(f"Circle Area: {circle.area()}")
print(f"Circle Perimeter: {circle.perimeter()}")