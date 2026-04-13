def square_decorator(func):
    def wrapper(a, b):
        result = func(a, b)  
        return result ** 2   
    return wrapper


@square_decorator
def add(a, b):
    return a + b


@square_decorator
def sub(a, b):
    return a - b


print("Square of add:", add(5, 3))  
print("Square of sub:", sub(5, 3))   