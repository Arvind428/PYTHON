"""
List is a built-in data structure used to store an ordered collection of items.
They are dynamic, resizable and capable of storing multiple data types.
Allows duplicate elements
Mutable
Creating a List
Lists can be created in several ways, such as using square brackets [] , the list() constructor or by repeating elements.
.Using Square Brackets: Square brackets [] are used to create a list directly.

. Using list() Constructor: A list can also be created by passing an iterable 
(such as tuple, string or another list) to the list() constructor.

"""
a = [1, 2, 3, 4, 5] #int
b = ['apple', 'banana', 'cherry']#string
c = [1, 'hello', 3.14, True] # mixed

print(a)
print(b)
print(c)



a = list((1, 2, 3, 'apple', 4.5))  
print(a)
b = list("GFG")
print(b)