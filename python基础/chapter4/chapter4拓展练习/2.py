import random

c = [random.randint(10, 100) for i in range(10)]
print(c)
print("平均数为：", sum(c) / 10)
dayu = [i for i in c if i > sum(c) / 10]
print(dayu)
