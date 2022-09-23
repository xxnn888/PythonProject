import random

a = random.randint(1, 100)
b = random.randint(1, 100)
c = random.randint(1, 100)

print(a, b, c)
if a >= b & b >= c:
    print("a > b > c", a, b, c)
if b >= a & a >= c:
    print("b > a > c", b, a, c)
if c >= b & b >= a:
    print("c > b > a", c, b, a)
if c >= a & a >= b:
    print("c > a > b ", c, a, b)
if a >= c & c >= b:
    print("a > c > b", a, c, b)
if b >= c & c >= a:
    print("b > c > a", b, c, a)
