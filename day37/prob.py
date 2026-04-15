#functions
def count_vowels(s):
    count=0
    for char in s:
        if char in ["a","e","i","o","u","A","E","I","O","U"]:
            count+=1
    return count
print(count_vowels("arvind"))