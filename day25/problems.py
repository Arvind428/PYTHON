#11111111111111111111111111111111111111111111111111111111#

# we can use single or double quotes for decalring a string
my_str1='Hello'
my_str2="World"
#Multi line string
my_str3="""
this is a 
multi line string 
"""
my_str4='''This is another
multi line string
'''

print(my_str1)
print(my_str2)
print(my_str3)
print(my_str4)

#How to check whether a word is present in a string or not
# examples

my_str="Hello World"
print('Hello' in my_str)# True
print('hey'in my_str)#False
print('H'in my_str)#True

# To know the length of a string
print(len(my_str))#11

#Printing with the help of indexing
#Positive indexing
print(my_str[0])  # H
print(my_str[6])  # W

#Negative Indexing
print(my_str[-1])#d
print(my_str[-4])#o

#IN Python all data types are treated as objects
#where as in the other languages it does not worklike that

#IMMUTABLE DATATYPES
#these are the datatypes which cannot be modified once declared.
# Strings are immutable datatypes in Python 
# Which means we can reassign a different string but we cannot directly modify the string

#EXAMPLE
greeting='hi'
greeting="hello"
print(greeting)# hello

greeting='hi'
#greeting[0]='H'
# we get this error
#     greeting[0]='H'
#     ~~~~~~~~^^^
# TypeError: 'str' object does not support item assignment
