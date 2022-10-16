a = set()
b = input()
num = 0
for i in range(len(b)):
    if b[i] == " ":
        a.add(b[num:i + 1:])
        num = i + 1
print(sorted(a))
