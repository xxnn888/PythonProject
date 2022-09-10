# print(3 > 5 and a > 3)  # 注意，此时并没有定义变量a
#
# print(3 > 5 or a > 3)  # 3>5的值为False,所以需要计算后面表达式  NameError: name 'a' is not defined
#
# print(3 < 5 or a > 3)  # 3<5的值为True,不需要计算后面表达式

print(3 and 5)  # 最后一个计算的表达式的值作为整个表达式的值  5

print(3 and 5 > 2)

print(3 not in [1, 2, 3])  # 逻辑非运算not

print(3 is not 5)  # not的计算结果只能是True或False之一

print(not 3)

print(not 0)
