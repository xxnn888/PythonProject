dict0 = {"one": 1, "two": 2, "three": 3}
for i in dict0.keys():
    print(i)
for i in dict0.values():
    print(i)
dict0['four'] = 4
print(dict0)
del dict0['four']  # 删除字典元素
print(dict0)

print(dict0.pop("three"))  # 删除并返回
