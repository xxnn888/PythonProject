# 输入一个数，判断是否为回文数
a = input("输入一个三位数：")
b = list(a)
if b[0] == b[2]:
    print(a, "是回文数")
else:
    print(a, "不是回文数")
