
str = input()
str2 = list(str)
print(str2)
a = 0
b = 0
for i in str2:
    if i >= 'A' and i <= 'Z' or i >= 'a' and i <= 'z':
        a += 1
    elif '0' <= i <= '9':
        b += 1
print("字母", a)
print("数字", b)
