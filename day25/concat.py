#222222222222222222222222222222222222222222222#

# WHAT IS STRING CONCATENATION
"""
you can combine multiple strings together with the plus (+) operator. 
This process is called string concatenation
"""
my_str_1 = 'Hello'
my_str_2 = "World"
str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str) # Hello World
#-----------------------------#
name = 'John Doe'
age = 26
name_and_age = name + age
print(name_and_age)
# we cannot concatenate a string and integer
#the reason for this thing is python does not automatically convert all elements into string
# we have to manually convert them into string like str(age)

name = 'John Doe'
age = 26
name_and_age = name + str(age)
print(name_and_age)

# we can also use assignment operator for concatenation
#represented by=+
name = 'John Doe'
age = 26

name_and_age = name#start with name
name_and_age += str(age)# append the age as string
print(name_and_age)

#INTERPOLATION
# The processof inserting variables and expressions into a string is called string interpollaation

#Python has a category of string called f-strings(short for formatted string literals)
#the f strings allows us to handle intepollaation with a compact and readable syntax

#F-strings start with f before the quotes and allow you to embed vaariables or expressions inside replacement fields indicated by curly braces{}
# here is an example
name = 'John Doe'
age = 26

name_and_age =f'My name is {name} and I am {age} years old'
print(name_and_age)
