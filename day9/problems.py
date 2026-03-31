#Take two numbers as input and print their sum, difference, product, and quotient.
a=int(input("enter 1st value"))
b=int(input("enter 2nd value"))
print(a+b)
print(a-b)
print(a/b)
print(a*b)

name=input("enter ur name")
age=int(input("enter your age"))
age10=age+10
print(f"Hello {name} You will be {age10} in 10 years")
#(Formula: F = C × 9/5 + 32)
temp=int(input("Enter the tempereature in celcius:"))
new_temp= temp*9/5+32
print(new_temp)
price=float(input("enter the price"))
dis=float(input("enter the discount"))
v=(dis/100)*price
print(price-v)

#circle area (pi*r*r) and circumferance(2*pi*r)
r=int(input("enter the radius of circle"))
pi=3.14159
area=pi*r*r
cir=2*pi*r
print(f"The area of circle is {area} and circumferance of circle is {cir}")

i=int(input("enter 4 digit num"))
d1=i//1000
d2=(i//100)%10
d3=(i//10)%10
d4=i%10
print(d1,d2,d3,d4)
total=d1+d2+d3+d4
print(f"the sum if all digits is {total}")
dist=float(input("Enter the distance in km:"))
time=float(input("Enter the time in hours:"))
avg_speed=dist/time
print(avg_speed)
m=int(input("marks obtained in math"))
p=int(input("marks obtained in phy"))
c=int(input("marks obtained in chem"))
total=m+p+c
perc=(total/300)*100
print(perc)

p=float(input("enter the principal amount"))
r=float(input("enter the rate of interest"))
t=float(input("time to clear the loan"))
SI=(p*r*t)/100
print(SI)


cost=100
sell=130
profit=sell-cost
print(profit)
loss=cost-sell
print(loss)