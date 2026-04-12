
#augumented assignments

#the agumented assignment helps us to store the value into the same variable without decealring a new variable

#syntax of an agumented assignments 
# variable <operator> = value
#more efficient way to do this is
#variable = variable <operator> value

my_var=10#here we are assigning the value
my_var+=5#here we are adding the value directly to the variable
print(my_var)#15

# another way of doing this is 
my_var=10# assign
my_var=my_var+5 #here we are taking the my_var value and adding +5 to it
print(my_var)#15

#in a similar way all we can use all the operators as an agumented operators


#SUBTRACTION

count=14
count-=3
print(count)#11

#MULTIPLICATION

#multiplies left variable with the right and stores back into the same result
product=13
product*=3
print(product)

#DIVISION
#divides the left variable with the right variable and stores back into the same result
price=100
price/=4
print(price)


#FLOOR DIVISION
pages=23
pages//=4
print(pages)

#MODULO
bits=23
bits%=3#23 is divided by 3 and we get the remainder
print(bits)

#EXPONENT
power=2
power**=3
print(power)#2 power 3 =8

#STRING CONCATENTAION
greet="Hello"
greet+=" World"
print(greet)# Hello World

#REPETITION OF STRINGS
hello="Hi"
hello*=5
print(hello)

#Type error for non compatable operators like sub and div


#Main point
#writing x++ in python just applies unary twice
#the python does not increment using X++ or ++x
# we should write x+=1
#which is more good to understand for programers later

x=6
print(+x)#6
print(++x)#6
x+=1
print(x)#7
x+=6
print(x)#7+6=