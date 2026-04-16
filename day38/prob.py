# print 1 to n numbers using functions
def num(n):
    for i in range(1,n+1):
        print(i)
num(6)

#using reccursion
def mun(s):
    if s==0:
        return
    mun(s-1)
    print(s)
mun(5)

def mu(s):
    if s==0:
        return 0
    return s+mu(s-1)
print(mu(5))
