import random

c = []
sum = 0
for i in range(10):
    a = random.randint(10, 99)
    c.append(a)
    sum += c[i]
    print(c[i])
print("平均数为：", sum / 10)
for j in range(10):
    if c[j] > sum / 10:
        print(c[j])
