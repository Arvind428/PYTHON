#Problem 1 — Vowel Counter with Grade
#Take a string input. Count the vowels. If vowels > 5, print "Vowel Rich", if 3–5 print "Moderate", else print "Vowel Poor".

# Input:  "programming is fun"
# Output: Vowels: 5 → Moderate
"""
#Problem 1 — Vowel Counter with Grade
#Take a string input. Count the vowels. If vowels > 5, print "Vowel Rich", if 3–5 print "Moderate", else print "Vowel Poor".

# Input:  "programming is fun"
# Output: Vowels: 5 → Moderate

#Problem 2 — Word Length Filter
#Take a sentence. Print only words that have more than 4 characters, in UPPERCASE.

# Input:  "I love python coding daily"
# Output: PYTHON  CODING  DAILY

#Problem 3 — Caesar Cipher (Shift by 3)
#Take a string. Shift every letter forward by 3 positions (a→d, b→e, z→c). Leave spaces as-is.
# Input:  "hello world"
# Output: "khoor zruog"

vowels='AEIOUaeiou'
x=str(input())
has_vowel=False
count=0
for char in x:
    if char in vowels:
        has_vowel=True
        count+=1

if count>=5:

    print("Vowel Rich")
elif count>=3 and count<=5:
    print("Moderate")
else:
    print("Vowel Poor")
"""


#Problem 2 — Word Length Filter
#Take a sentence. Print only words that have more than 4 characters, in UPPERCASE.

# Input:  "I love python coding daily"
# Output: PYTHON  CODING  DAILY

#sentence=input("Enter the sentence: ")
#words=sentence.split()
#for word in words:
 #   if len(word)>4:
 #       print(word.upper())


 #Problem 3 — Caesar Cipher (Shift by 3)
#Take a string. Shift every letter forward by 3 positions (a→d, b→e, z→c). Leave spaces as-is.
# Input:  "hello world"
# Output: "khoor zruog"




 
