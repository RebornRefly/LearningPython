from random import randint

lst = []
for number in range(10):
    lst.append(randint(1, 10))
print(lst)
result = []
for i, e in enumerate(lst):
    if e % 2 == 0:
        lst[i] = 'even'
print(lst)
