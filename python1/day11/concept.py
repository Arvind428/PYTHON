"""
FOR loop
for loop is used to iterate over a sequence such as a list,tuple,string or 
range.It allow to execute a block of code repeatedly,once for each item
in the sequence.


n = 4
for i in range(0, n):
    print(i)

Explaination:
the code prints the numbers from 0-3 using a loop that iterattes over a range 
from 0 to n-1 

out:
0
1
2
3

While loop:

In Python 
a while loop is used to execute a block of statements repeatedly until
a given condition is satisfied .
When the condition become false,
the line immediately after the loop in the program is executed.

cnt = 0
while (cnt < 3):
    cnt = cnt + 1
    print("Hello Geek")

Infinite While Loop :
If we want a block of code to execute infinite number of times
 then we can use the while loop in Python to do so.

 
 while(True):
    print("hello Geek")

    
Nested Loops:
Python programming language allows to use 
one loop inside another loop which is called nested loop

for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()

"""