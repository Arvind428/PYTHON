def dec(func):
    def wrapper(a,b):
        result=func(a,b)
        return (result*result)
    return wrapper

@dec
def add(a,b):
    return a+b
@dec
def sub(a,b):
    return a-b

print(add(2,3))
