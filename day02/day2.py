#variable:it is a name given to a memory location to store data
#ex:
x=20
name="arvind"

#How can we print variables
#ex:
print(name)
print("my age is:",x)
"""
        Python is dynamically typed 
    1.we dont need to declare variable
    2. It can uderstand thhe datatype during the runtime
    3.it automatically decides at the run time
    
    PYTHON
    python has builtin datatypes
    the data types are of 2 types
    mutable:can change the value after creation.
    immutable:cannot change the value after creation.
    datatypes are:
    int
    float
    str
    boolean
    complex
    list
    tuple
    set
    dictionary
    none
"""
#int(whole numbers either positive or negative)
a=10
b=-5
print(a,b)
#float(decimal,values)
marks=7.4
price=24.9
print(marks,price)
#string(text data  enclosed in quotes)
name="arvind"
course='B-tech'
#boolean(true/false)
student=True
passed=False
#used in decision making
#none type(represents no value)
manoj=None
print(manoj)
#multiple variable assignment
a=b=c=10
#multiple variable assignment
x,y,z=1,2,3
print(a,b,c)
print(x,y,z)
#complex
a=3+4j
print(a)
print(type(a))

#list(square brackets)
#A list is a built in data type in python used to store multiple values in a single variable
'''
Key Features of List:
>Ordered
>Mutable(can be changed)
>Can store different data types
'''
#example:
data=[10,3.5,"python",True]
print(data)
print(type(data))

'''
#tuple(same as list but enclosed with paranthesis)
>Oredered
>immutable
'''
#ex:
t=(1,2,3)
print(t)
print(type(t))

#set
#unordered
#no duplicates
s={1,2,3,3}
#it does not print duplicates even if we stored in the sourse code
print(s)

#dictonary
#stores data as key-value pairs
student={
    "name":"Arvind",
    "age":20
}
y=10
print("class of 10 is")
print(type(y))#type function is used to get datatype of a variable
#int datatype
z=10.6
print("class of 10.6 is")
print(type(z))
#float datatype
q="Arvind"
print("class of Arvind is")
print(type(q))
#string datatype
#python is case sensitive
m=13
M="Vinay"
print(M)#prints value of B
print(m)#prints value of b