from random import randint

lst = []
for i in range(10):
    lst.append(randint(1, 100))
print(lst)
result = ['Even' if n % 2 == 0 else 'Odd' for n in lst]
print(result)
