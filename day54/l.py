cities = ['Los Angeles', 'London', 'Tokyo']

cities = ['Los Angeles', 'London', 'Tokyo']
cities[0] # 'Los Angeles'

cities = ['Los Angeles', 'London', 'Tokyo']
cities[-1] # 'Tokyo'

developer = 'Jessica'
list(developer) # ['J', 'e', 's', 's', 'i', 'c', 'a']

numbers = [1, 2, 3, 4, 5]
len(numbers) # 5

programming_languages = ['Python', 'Java', 'C++', 'Rust']
programming_languages[0] = 'JavaScript'
print(programming_languages) # ['JavaScript', 'Java', 'C++', 'Rust']

programming_languages = ['Python', 'Java', 'C++', 'Rust']
programming_languages[10] = 'JavaScript'

"""
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
IndexError: list assignment index out of range
"""

# you want to remove an element from a list you can use the del keyword like this:

developer = ['Jane Doe', 23, 'Python Developer']
del developer[1]
print(developer) # ['Jane Doe', 'Python Developer']

programming_languages = ['Python', 'Java', 'C++', 'Rust']

# 'Rust' in programming_languages # True
# 'JavaScript' in programming_languages # False
