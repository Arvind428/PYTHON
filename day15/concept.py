#list comprehesion
"""
List comprehension is just a shorter way to create a list in Python.
Instead of writing a full loop, you write everything in one line
Example — get squares of numbers:
# Normal way
squares = []
for x in range(5):
    squares.append(x**2)

# List comprehension way
squares = [x**2 for x in range(5)]
Both give the same result: [0, 1, 4, 9, 16]
That's all it is — same logic, just shorter.
"""
# BAsic ist comprehension
x=int(input())
square=[x**2 for x in range(1,x+1)]
print(square)
# using if condition in for loop
x=int(input())
even=[x for x in range(x) if x%2==0]
print(even)
#using if else condition
x=[1,2,4,6,8,2,341,6,56]
even=[f"{i} even" if x%2==0 else f"{i} odd" for i,x in enumerate(x)]
print(even)
#----------------------------------------------------------------------------------------------------------------------------
# BASIC DECORATOR
