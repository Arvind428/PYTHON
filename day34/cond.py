"""
How Do Conditional Statements and Logical Operators Work?

We know that we only have two values in a boolean statements 
they are True and False

The comparision operators in Python:

the operators are
==,!=,>,<,>=,<=
"""
print(3 > 4) # False
print(3 < 4) # True
print(3 == 4) # False
print(4 == 4) # True
print(3 != 4) # True
print(3 >= 4) # False
print(3 <= 4) # True

"""
if condition:
    pass # code to execute if condition is true
    if condition is an expression that evaluates to True or False follwed by a colon:

"""
#Example of if statement
age=56
if age>18:
    print("you are  adult")

#intendation error comes when you try to write print staement right below the if statement
# if age<18:
# print(age)
"""
  File "c:\Users\arvin\OneDrive\Desktop\PYTHON\day34\cond.py", line 33
    print(age)
    ^^^^^
IndentationError: expected an indented block after 'if' statement on line 32 
"""

