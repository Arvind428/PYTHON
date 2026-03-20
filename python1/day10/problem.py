num=int(input("enter the number"))
if (num>0):
    print("positive number")
elif(num==0):
    print("Zero")
else:
    print("negative")
#----------------------------------------------------#
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
if(num1>num2):
    print(f"{num1} is larger")
elif(num2>num1):
    print(f"{num2} is larger")
else:
    print("both are equal")

#---------------------------------------------------------#
cost = float(input("Enter cost price: "))
sell = float(input("Enter selling price: "))

diff = sell - cost
if diff > 0:
    print("Profit of", diff)
elif diff < 0:
    print("Loss of", abs(diff))
else:
    print("No profit, no loss")
#--------------------------------------------------------------#
year=int(input("enter the year"))
if ((year%4==0 and year%100!=0) or (year%400==0)):
    print(f"{year} is leap year")
else:
    print(f"{year} is not a leap year")
#---------------------------------------------------------#

a=int(input("enter the first num"))
b=int(input("enter the second num"))
c=int(input("enter the 3rd num"))
if (a>b  and a>c):
    print(f"{a} is largest number")
elif(b>a and b>c):
    print(f"{b} is the largest number")
elif(c>a and c>b):
    print(f"{c} is the largest number")
else:
    print(f"{a},{b},{c} are equal")
#-------------------------------------------------------#
marks=int(input("enter your marks"))
if (marks<=100 and marks>90):
    print("A")
elif (marks<=90 and marks>75):
    print("B")
elif (marks<=75 and marks>60):
    print("C")    
elif (marks<=60 and marks>50):
    print("D")
elif (marks<50):
    print("Fail")