#python tuples
"""
A tuple in python is an immutable ordered collection of elements


Creating a tuple 
A tuple is created by placing all the items inside parantheses(), seperated by commas.
A tuple can have any number  oof items and they can be of different data types
"""
tup = ()
print(tup)

# Using String
tup = ('Arvind', 'Goud')
print(tup)

# Using List
li = [1, 2, 4, 5, 6]
print(tuple(li))

# Using Built-in Function
tup = tuple('Arvind')
print(tup)