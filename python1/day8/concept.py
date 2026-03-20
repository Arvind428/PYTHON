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

#Ternary Operator
#this operatoer is also known as the conditinal operator
#Syntax: [on_true] if [expression] else[on_false]
a, b = 10, 20
min = a if a < b else b
print(min)


#Operator Precedence

"""
This is used in an expression with more than one operator with different
precedence to determine which operation to perform first.
"""
exp=10+20*30# *  (multiplication is first)
#              +  (addition is second)
print(exp)
name="Alex"
age=0

if name=="Alex"or name=="John" and age>=2:
# (and) operator always evaluates before (or) operator
# if(name=="Alex") or (name=="John" and age>=2): 
# we should use parantesis when mixing and,or operators
    print("Hello! Welcome.")
else:
    print("Good Bye!!")


#Priority Order

#1st= *,/,%     (arithematic)
#2nd=+-         (Arithematic)
#3rd= (==,!=,>=)   (Comparision)
#4th=and            (logical)
#5th= or        (logical)