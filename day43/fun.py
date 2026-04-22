t = (1, 2, 3, 4)
print(t)

t = (10, 20, 30, 40)
print(t[0])   # First element
print(t[-1])  # Last element

t = (5, 10, 15, 20)
print(len(t))

t = (1, 2, 3, 2, 4, 2)
print(t.count(2))

t = (10, 20, 30, 40)
print(t.index(30))

t = (10, 20, 30, 40, 50)
print(t[1:4])

t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2
print(t3)

t = (1, 2)
print(t * 3)

t = (1, 3, 5, 7)
print(5 in t)

l = [1, 2, 3]
t = tuple(l)
print(t)

t = (10, 20, 30)
a, b, c = t
print(a, b, c)