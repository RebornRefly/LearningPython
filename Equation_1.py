from math import sqrt

# 2x²+5x-8=0,x=?
a = 2
b = 5
c = -8
d = b ** 2 - 4 * a * c
x1 = (-b + sqrt(d)) / 2 * a
x2 = (-b - sqrt(d)) / 2 * a
print('x1 = {0},x2 = {1}'.format(x1, x2))
