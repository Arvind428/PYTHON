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