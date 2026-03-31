""""
Strings are sequence of characters written inside quotes
It can include letters, numbers, symbols and spaces.
Python does not have a separate character type.
Strings are commonly used for text handling and manipulation.

Creating a String
Strings can be created using either single ('...') or double ("...") quotes. Both behave the same.
Example: Creating two equivalent strings one with single and other with double quotes.


Multi-line Strings
Use triple quotes ('''---''' ) or ("""""") for strings that span multiple lines. Newlines are preserved.
Example: Define and print multi-line strings using both styles.

Accessing characters in String
Strings are indexed sequences. Positive indices start at 0 from the left, negative indices start at -1 from the right

"""

#Creating a String

s1 = 'Arvind'  
s2 = "Goud"  
print(s1)
print(s2)

#

s = """I am Learning
Python String for AI Enginner Role"""
print(s)

s = '''I'm  
Arvind'''
print(s)

s = "Arvind and vinay"
print(s[0])   
print(s[4])