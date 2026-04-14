# implement arithmatic operation using functions

def arth(a,b):
    print("Addition",a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a//b)
    print(a%b)

arth(5,6)


def test(m,n):
    return m+n,m-n,m*n,m/n,m//n,m%n

print(test(5,6))
# check even or odd for the given number using functions
def eo(n):
    if n%2==0:
        print(f"{n} is even")
    else :
        print(f"{n} is odd")

eo(6)

def test1(x):
    return x