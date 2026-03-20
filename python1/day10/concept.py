"""
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
#Example

#for=10
#    print(for)