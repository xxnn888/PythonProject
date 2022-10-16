str = input("输入一个字符串:")

for i in range(len(str)):
    print(f"第{i}个字符的编码是{ord(str[i])}")
dict1 = {i + "字符的编码是：": ord(i) for i in str}
print(dict1)
