# def multiplicationTable(N):
#     for i in range(1, 11):
#         print(i * N, end=" ")
# #-------------------------------------------------------------------------------------------------------------------------------------
# #User function Template for python3
# n = int(input())
# for i in range(1,11):
#     print(i*n,end=" ")
# #-------------------------------------------------------------------------------------------------------------------------------------

# def stringJumper(s):
#     for i in range(0,len(s),2):
#         # from 0 to length of str and skip 2
#         print(s[i], end="")
#         #printing character and separating characters by nothing
# #-------------------------------------------------------------------------------------------------------------------------------------
# #User function Template for python3
# x = int(input())
# while (x>=0):
#     print(x,end=" ")
#     x-=1
#------------------------------------------------------------------------------------------------------------------------------------
def printIncreasingPower(x):
    #code here
    i=1
    # Loop to jump in powers of 2
    while(i*i<=x):
        print(i*i,end=" ")
        i+=1
#------------------------------------------------------------------------------------------------------------------------------------