# print 1 to n numbers using functions

def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)   # recursive call
    print(n)
print_numbers(5)

#reverse a string using functions --str = "Hello"
def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]
str_val = "Hello"
print(reverse_string(str_val))