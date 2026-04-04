#3333333333333333333333333333333333#

#WHAT IS STRING SLICING
# string slicing lets you extract a portion of a string or work with only a specific part of it

#Syntax 
# string[start:stop]
str="Hello World"
print(str[0:4])#Hell
#We can print from start by skipping start indice
print(str[:4])#Hell
#printing from start to end indice
print(str[4:])#o world

# we can also get every even sting index if wwe want
#Synatx is string[start:stop:step]
# example
print(str[0:11:2])#HloWrd
#useful tip
#We can reverse a string by using this syntax
print(str[::-1])#dlorw olleH

#STEP OPERATOR specifies the increment between each characte to extract
