#Python Functions are a block of statements that does a specific task. 
# The idea is to put some commonly or repeatedly done task together and make a function
#  so that instead of writing the same code again and again for different inputs, 
# we can do the function calls to reuse code contained in it over and over again.

# CREATING A FUNCTION

def fun():
    print("Welcome to GFG")
    
fun()

#Function Arguments

def evenOdd(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(evenOdd(16))
print(evenOdd(7))

#Types of Function Arguments

#1. Default Arguments: 
# A default argument is a parameter that assumes a default value if a value is not provided in the function call for that argument.
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)

myFun(10)

#2. Keyword Arguments: 
# values are passed by explicitly specifying the parameter names, so the order doesn’t matter.

def student(fname, lname):
    print(fname, lname)

student(fname='Geeks', lname='Practice')
student(lname='Practice', fname='Geeks')


#3. Positional Arguments: values are assigned to parameters based on their order in the function call.
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

print("Case-1:")
nameAge("Olivia", 27)

print("\nCase-2:")
nameAge(27, "Olivia")

