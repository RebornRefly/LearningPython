a = [1, 3, 5, 7, 9]
b = [2, 4, 6, 8, 10]
c = []
print(list(zip(a, b)))
for x, y in zip(a, b):
    c.append(x + y)
print(c)

a1 = [1, 3, 5]
b1 = [2, 4, 6, 8]
c1 = []
print(list(zip(a1, b1)))
