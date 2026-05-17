#Problem 1

# Create a base class Animal.

# Subclasses:

# Dog
# Cat

# Each class should implement: sound method()
# Expected:

# Dog → "Bark"
# Cat → "Meow"

class Animal:
    def sound(self):
        print("Animal Sound")
class Dog(Animal):
    def sound(self):
        print("Bark")
class Cat(Animal):
    def sound(self):
        print("Meow")

d1=Dog()
c=Cat()
d1.sound()
c.sound()

# Problem 2

# Create base class:Employee
# Subclasses:
# Manager
# Developer
# Intern

# Each employee has:

# name
# salary

# Manager gets bonus salary.

# Developer gets project allowance.

# Intern gets stipend.


class Employee:
    def id(self,name,salary):
        print("should have an employee id")
class manager(Employee):
    def id(self,name,salary):
        print(f"manager {name} gets salary of {salary}")
        print("manager gets bonus salary")
        print("final Salary",salary+5000)
class developer(Employee):
    def id(self,name,salary):
        print(f"developer {name} gets salary of {salary}")
        print("Developer gets project allowance")
        print("final Salary",salary+3000)
class intern(Employee):
    def id(self,name,salary):
        print(f"intern {name} gets salary of {salary}")
        print("Intern gets the stipend")
        print("final Salary",salary+2000)
        
m=manager()
d=developer()
i=intern()

m.id("bharadwaj",500000)
d.id("pavani",100000)
i.id("arvind",15000)

# Problem 3

# Create abstract class:

# Shape

# Abstract method:

# area()

# Subclasses:

# Circle
# Rectangle
# Triangle

# Calculate respective areas.

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        