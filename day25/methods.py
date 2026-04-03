#Methods in Strings
str="ArvInd"
print(str.upper())
#string.upper() is used to upper case in the string
print(str.lower())
#string.lower() is used to lower case in the string

str1="  Hello World     "
print(str1)
print(str1.strip())
# string.strip() returns a new string with specified leaading and trailing characters removed
#if no argument is passed it removes leading and trailing whitespaces(Spacebars)

print(str1)
str2=str1.replace('Hello','hi')
print(str2)#hi world
# the string.replace(old,new) replaces the particuar string with new string in that space or index

s="i wanna become and AI engineer"
print(s.split())
#split(seperator):Splits a string on a specified seperator into a list of strings.
#If no seperator is specified, it splits on whitespace

l=['i', 'wanna', 'become', 'and', 'AI', 'engineer']
print(' '.join(l))
#join(iterable) Joins elements of an iterable into a string with a separator.

hello="arVind goud"
print(hello.startswith("arvind"))#True
#startswith(prefix): Returns a boolean indicating if a string starts with the specified prefix.

print(hello.endswith("goud"))
#endswith(suffix): Returns a boolean indicating if a string ends with the specified suffix.

print(hello.find("Goud"))#7
print(hello.find("t"))
#find(substring): Returns the index of the first occurrence of substring, or -1 if it doesn't find one

print(hello.count('d'))#2
#count(substring): Returrns the number of time a substring appears in a string

print(hello.capitalize())
#capitalize(): Returns a new string with the first character capitalized and the other characters lowercased.

new="i am a python developer"
print(new.isupper())
#isupper(): Returns True if all letters in the string are uppercase and False if not.

print(new.islower())
#islower(): Returns True if all letters in the string are lowercase and False if not.

print(new.title())