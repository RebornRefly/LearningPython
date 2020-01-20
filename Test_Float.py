import decimal
import fractions

# Normally calculate 0.1 + 0.2, there will be some problems.
print(0.1 + 0.2)  # 0.30000000000000004

# As we can see, the number after the dot are too long.
# We can use import decimal package to solve it.
print(decimal.Decimal('0.1') + decimal.Decimal('0.2'))  # 0.3

# About fractions
print(fractions.Fraction(2, 5) + fractions.Fraction(3, 5))  # 1

# Pay attention, all these calculation can be used in normal math calculate.
a = decimal.Decimal('0.1')
b = decimal.Decimal('0.2')
c = fractions.Fraction(2, 5)
print(a + b + 2)
print(3 + c)

# But, can't use these in following usage.
# print(a + b + 2.5)
# print(b + c)
