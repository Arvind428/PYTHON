#integers and floats are the primary numeric data types in Python 
#With them , we can store numeric data and perform mathematical operations

num1=5
num2=10
print("1",num1+num2)#Addition
print("2",num1-num2)#subtraction
print("3",num1*num2)#Multiplication
print("4",num1/num2)#division
print("5",num1%num2)#modulo
print("6",num1//num2)#floor division
print("7",num1**num2)#Exponentiation
print("8",float(num1))
flt1=6.5
flt2=4.6
print(flt1+flt2)#float Addition
print(flt1-flt2)#Float subtraction
print(flt1*flt2)#Float Multiplication
print(flt1/flt2)#float division
print(flt1%flt2)#float moodulo
print(flt1//flt2)#float floor division
print(flt1**flt2)#float exponentiation
print(int(flt1))

#Floor division divides two numbers and returns the greatest integer less than or equal to the result. This is done with the double forward slash operator (//):

#round(): Rounds a number to the specified number of decimal places.
# By default this function rounds to the nearest integer,
#  and returns a whole number with no decimal places:

myint1=21.452
myint2=23.634
print(round(myint2))

#abs(): returns the absolute value of a number
num=-13
print(abs(num))

#pow(): raises a number to the power of another or performs modular exponentiation
res1=pow(4,2)# 4**2
print(res1)
res2=pow(2,3,5)#(2**3)%5
print(res2)