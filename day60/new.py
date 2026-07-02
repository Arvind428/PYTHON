a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum =", a + b)

num = int(input("Enter a number: "))


if num % 2 == 0:
    print("Even")
else:
    print("Odd")


#reverse a string
text = input("Enter a string: ")
print(text[::-1])

#find the largest number in list
numbers = [4, 7, 1, 9, 3]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print(largest)

#count vowels
text = input("Enter a string: ")

count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1
print("Vowels:", count)

