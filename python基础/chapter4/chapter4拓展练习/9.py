str = input()
a = 0
b = 0
c = 0
d = 0
for i in list(str):
    if i >= 'A' and i <= 'Z' or i >= 'a' and i <= 'z':
        a += 1
    elif '0' <= i <= '9':
        b += 1
    elif i == ' ':
        c += 1
    else:
        d += 1
print("字母：%d 数字：%d 其他字符：%d 空格：%d" % (a, b, c, d))
