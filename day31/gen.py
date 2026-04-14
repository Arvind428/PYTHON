#Generators---------
#It is special type of a function that returns values one by one 
#instead of returning everything at once

"""
def num():
    print(1)
    print(2)
     

n = num()
print(n)
"""
"""
def num():
    return [1,2,3]
print(num())
"""
"""
def num():
    yield 1
    yield 2
    yield 3

#print(num())
for i in num():
    print(i)
"""
#advantages---
#memory efficient
#Faster
#useful for large data

# input =5
#output =
#0
#1
#4
#9
#16
"""
def square(n): # user i/p
    for i in range(n): # 0,1,2,3,4
        yield i*i #0,1,4,9,16

    

n = int(input())#i/p 
for j in square(n):#
    print(j)
    
"""
"""
def num():
    yield 1
    yield 2
    yield 3

n = num()

print(next(n))
print(next(n))
print(next(n))
"""

#problems on generators----

# print the one by one values as per the user input --
# input: 100
# output: line by line values which are divisible by 3



def div3(n):
  for i in range(2, n + 1):
    if i % 3 == 0:
      yield i
hi=div3(int(input()))
for v in hi:
    print(v)
