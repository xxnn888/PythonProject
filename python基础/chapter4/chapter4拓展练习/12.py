import random

a = random.randint(1, 10)
b = 0
for i in range(3):
    print("输入一个数：")
    b = int(input())
    if b == a:
        print("猜对了！！！")
        break
    else:
        print("错误，，请重新输入")
