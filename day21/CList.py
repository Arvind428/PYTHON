"""List is a built-in data structure used to store an ordered collection of items. They are dynamic, resizable and capable of storing multiple data types.

Allows duplicate elements
Mutable: list elements can be changed, updated, added, or removed after the list is created.
Ordered: elements maintain the order in which they are inserted.
Index-based: elements are accessed using their position, starting from index 0.
Heterogeneous: a list can store different data types such as integers, strings, booleans and even other lists.

Creating a List
Lists can be created in several ways, such as using square brackets [] , the list() constructor or by repeating elements.

1. Using Square Brackets: Square brackets [] are used to create a list directly.


a = [1, 2, 3, 4, 5] # List of integers
b = ['apple', 'banana', 'cherry'] # List of strings
c = [1, 'hello', 3.14, True] # Mixed data types

print(a)
print(b)
print(c)


a = list((1, 2, 3, 'apple', 4.5))  
print(a)

b = list("GFG")
print(b)


a = [2] * 5
b = [0] * 7

print(a)
print(b)
"""