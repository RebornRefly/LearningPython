from math import cos, degrees, radians

# a=3,b=7,c=9,∠A=?,∠B=?,∠C=?
a = 3
b = 7
c = 9
cos_c = (a ** 2 + b ** 2 - c ** 2) / 2 * a * b
cos_b = (a ** 2 + c ** 2 - b ** 2) / 2 * a * c
cos_a = (b ** 2 + c ** 2 - a ** 2) / 2 * b * c
print(cos(cos_c))
print(cos(cos_b))
print(cos(cos_a))
