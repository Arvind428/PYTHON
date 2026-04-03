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
# name_and_age = name + age
# print(name_and_age)
# we cannot concatenate a string and integer
#the reason for this thing is python does not automatically convert all elements into string
# we have to manually convert them into string like str(age)

name = 'John Doe'
age = 26
name_and_age = name + str(age)
print(name_and_age)