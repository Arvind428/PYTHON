def decorator(abc):
    def bat3():
        for i in range(10):   # give some value to n
            if i % 2 == 0:
                print("even number", i)
        abc()
    return bat3 
@decorator
def prime():
    print("Hello")
prime()