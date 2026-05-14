"""
what is a function:
functions are resusavle pieces of code that run when you call them.
Many programming languages come with built-in functions that make it easier to get started.
"""

#syntax for functons
def calculate_sum(a,b):
    print(a+b)

calculate_sum(4,2)#6
# if we call the functions without the correct arguments then we will get an type error
"""calculate_sum()"""
#TypeError: calculate_sum() missing 2 required positional arguments: 'a' and 'b
sum=calculate_sum(3,1)
print(sum)#4
"""
SUMMARY
default value of the return function is None 
Arguments are the values we pass to a function when you call it
parameter is the term for a placeholder variable in a function
"""

"""
SCOPE:
It determines the point at which we can access a variable.
Python follows the LEGB rule:
Local scope(L): Variable sdefined in functions or classes
Enclosing scope(E):variables defined in enclosing or nested function
Global Scope(G):Variables defined at the top level of the module or file
Built-in scope(B):Reserved names in Python for predefined functions,modules,keywords and objects
"""

#Local scope
#It means a variable declared inside a fuunction or class can only be accessed within that function or class
print("Local Scope")
def my_func():
    my_var=10#locally scoped to my_finc
    print(my_var)
my_func()#10

#print(my_var)#NameError: name 'my_var' is not defined

#because the my_var is declared inside the function

#Enclosing Scope
#It means that a function that's nested inside another function can access the variables of the function it's nested within
def outer_func():
    msg='Hello there!'

    def inner_func():
        y=20
        print(msg)#inner can access  outer variable
    inner_func()
    #print(y) gives NameError
    #outer cannot access inner variable
outer_func()

"""
In the above exaple the inner function can freely acceess
the msg variable defined in the outer function
But the outer function cannot access variables defined within any nested functions
"""
def outer():
    msg='Hello!'
    #print(res) it is a loccaly scoped to inner() the function tries to print res before inner is called
    
    def inner():
        res="how are you?"
        print(msg)
    inner()
outer()