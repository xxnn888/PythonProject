# int 函数的使用

from fractions import Fraction

print(int(-3.2))

x = Fraction(7, 3)
print(x)

Fraction(7, 3)
print(int(x))

print(int("0x22b", 16))

print(int(bin(54321), 2))

# print(int('0b111'))   ValueError: invalid literal for int() with base 10: '0b111'

print(int('0b111', 0))

# print(int('0b111', 6))   ValueError: invalid literal for int() with base 6: '0b111'

