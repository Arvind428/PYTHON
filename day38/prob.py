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
    else:
        return s+mu(s-1)
print(mu(5))
