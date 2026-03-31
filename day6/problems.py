'''Type conversion means changing one data type into another.

Python supports two types of type conversion:
1)Implicit Type Conversion
2)Explicit Type Conversion (Type Casting)'''

#Implicit Type Conversion:Python automatically converts one data type into another without user involvement.

#Example:
a=10
b=2.5
c=a+b
print(c)
print(type(c))

#Explicit Type Conversion
#Programmer manually converts data types using built-in functions.
#common type casting functions

#int() conversion
a=23.6
print(int(a))

#float() Conversion
a=45
print(float(a))

#str() conversion
a=21
print(str(a))

#complex() conversion
print(complex(2,3))

#bool() conversion
print(bool(0))
#operators
print(a+b)# addition