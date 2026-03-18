"""
Operators : Special symbols like +,-,/,* etc
Operands : VAlue on which the operator is applied

TYPES OF OPERATORS IN PYTHON

Arithmetic operators : +,-,*,%,/

Relational Operators : <,<=,>,>=,==,!=

Logical Operators : AND,OR,NOT

Bit wise Operators : &,|,^,~,<<,>>

Assignment Operator : =,+=.-=.*=,%=

"""

#ADDITION
a=4
b=10
print("Addition",a+b)
print("Subtraction",a-b)
print("multiplication",a*b)
print("Division",a/b)
print("FLoor Division:",a//b)
print("Modulus:",a%b)
print("Exponentiation",a**b)

#Comparison or Relational Operators
#returns either true or false
a = 13
b = 33

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

#Logical Operators
# performs logical AND,OR,NOT operations

a = True
b = False
print(a and b)
print(a or b)
print(not a)


#Bitwise Operators

a = 10
b = 4

print(a & b)#Bitwise AND
print(a | b)#OR
print(~a)#NOT
print(a ^ b)#XOR
print(a >> 2)#Right
print(a << 2)#Left

#Assignment Operators

a = 10
b = a# assigns value of a to b
print(b)
b += a# 
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a
print(b)


#Identity Operators
a = 10
b = 20
c = a
print(a is not b)
print(a is c)

#Membership Operators
#used to know whether a value or variable is in sequence or not
# in : True if value is found in the sequence
# not in True if value is not found in the sequence
x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")