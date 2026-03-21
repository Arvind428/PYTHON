
"""
Decorator is used when the same block of code needs to run before or after multiple functions, so you don't repeat it everywhere.
def decorator(birth):
    def dec_mate():
        print(birth().upper())
    return dec_mate()


@decorator
def birth():
    return "Happy Birth Day"
birth()
"""

"""
def decor(ad):
    def summ(a,b):
        #s = ad(a,b)
        return ad(a,b)*2
    return summ
    
@decor
def ad(a,b):
    return a+b

print(ad(2,3))
"""



# PYTHON KEYWORDS
import keyword
print("The list of keywords are : ")
print(keyword.kwlist)
"""
Keywords in Python are special reserved words that are part of the language itself.
They define the rules and structure of Python programs which means you cannot use them as
names for your variables, functions, classes or any other identifiers.

(Way to identify keywords)

with Syntax Highlighting : Most IDEs provide syntax-highlight feature.
We can see keywords appearing in different color or style

Look for Syntax Error: This error will encounter if u have used any keyword
incorrectly.Keywords can not be used as identifiers 
like variable or a function name
                        
"""



"""
If Conditional Statement:
If statement is the simplest form of a conditional statement. 
It executes a block of code if the given condition is true.

Short hand if:
age = 19
if age > 18: print("Eligible to Vote.")

------------------------------------------------------------------------------

If-else Conditinal statements
If Else allows us to specify a block of code 
that will execute if the condition(s)
associated with an if or elif statement evaluates to False.
Else block provides a way to handle all other cases 
that don't meet the specified conditions.

------------------------------------------------------------------------------
elif Statement
elif statement in Python stands for "else if."
It allows us to check multiple conditions,
providing a way to execute different blocks of code
based on which condition is true. 
Using elif statements makes our code more readable and efficient
by eliminating the need for multiple nested if statements.


------------------------------------------------------------------------------------
Nested if..else Conditional Statement
Nested if..else means an if-else statement inside another if statement. 
We can use nested if statements to check conditions within conditions.
-----------------------------------------------------------------------------------


Match-Case Statement
match-case statement is Python's version of a switch-case found in other languages.
 It allows us to match a variable's value against a set of patterns.

number = 2

match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")




"""