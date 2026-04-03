#multiple variable
a=b=c=10
print(a)
print(b)
print(c)

#data type
age=20
marks=15.5
name="Arvind"
print(type(age))
print(type(marks))
print(type(name))

#age after 5years
age=20
print(int(age)+5)

#multiple assignment
age,name,marks=17,"Arvind",15.5
print("age:",age)
print("name:",name)
print("marks:",marks)

#swapping (using temp variable)
a=5
b=10
temp=a # we store a value in temp variable
a=b # we overide the a value with b
b=temp # the stored value in temp is given to b
print(a,b) # the num gets swapped
#without using temporary variable
a=5
b=10
a,b=b,a #we using tuple for this in ths case the (a,b)=(b,a) get changed acc to the index
print(a,b)
