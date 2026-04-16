# print 1 to n numbers using functions

def num(n):
    for i in range(1,n+1):
        print(i)

num(5)

#reverse a string using functions --str = "Hello"
def rev(st):
    st=st[::-1]
    print(st)

rev("Hello")