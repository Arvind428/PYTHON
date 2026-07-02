#print a string
text = input("Enter a string: ")
count = 0
for ch in text.lower():
    if ch in "aeiou":
        count += 1
print("Vowels:", count)

#input
text = input("Enter a string: ")
print(text)

#length
text = input("Enter a string: ")
print(len(text))

#first char
text = input("Enter a string: ")
print(text[0])

#last char
text = input("Enter a string: ")
print(text[-1])

#reverse string
text = input("Enter a string: ")
print(text[::-1])

