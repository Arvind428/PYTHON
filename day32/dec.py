#write a decorator to implement square of a number 
#  which was acquired by the 2 func add() & sub() these are outer functions
def square_decorator(func):
    def wrapper(a, b):
        result = func(a, b)  
        return result * result   
    return wrapper


@square_decorator
def add(a, b):
    return a + b


@square_decorator
def sub(a, b):
    return a - b
print(add(4,5))