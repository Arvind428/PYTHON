s = "hello world"
vowels = "aeiou"
count = 0

for letter in s:
    if letter in vowels:
        count = count + 1

print(count)

s = "aabbcd"

for letter in s:
    if s.count(letter) == 1:   
        print(letter)          
        break

s1 = "listen"
s2 = "silent"

# If both strings have same letters, sorted will give same result
if sorted(s1) == sorted(s2):
    print("Yes, they are anagrams")
else:
    print("No, they are not anagrams")