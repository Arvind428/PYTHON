#functions
#vowels counting
def count_vowels(s):
    vowels="aeiouAEIOU"
    count=0
    for char in s:
        if char in vowels:
            count+=1
    return count
print(count_vowels("arvind"))

#Palindrome
def is_palindrome(s):
    reversed=s[::-1]
    if s==reversed:
        return True

print(is_palindrome("dad"))

#printing even numbers
def sum_even(n):
    total=0
    for i in range(2,n+1):
        if i%2==0:
            total+=i
    return total
print(sum_even(4))

#word counting
def word_count(sentence):
    count=0
    x=sentence.split()
    for word in x:
        count+=1
    print(count)
word_count("we are friends and u dont know anything about me")

#largest word in sentence
def largest_word(large):
    y=large.split()
    for word in large:
        largest=len(word)
        if largest>len(word):
            largest=len(word)
        print(largest,word)
largest_word("we are this")