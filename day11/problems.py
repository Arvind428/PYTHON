for i in range(1, 21):
    if i % 2 == 0:
        print(i)
    else:
        print("odd")

n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)

n = input("Enter a number: ")
total = 0
for digit in n:
    total = total + int(digit)
print("Sum:", total)

for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

