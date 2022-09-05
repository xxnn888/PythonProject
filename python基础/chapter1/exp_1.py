# 作业：
# 1 输入两个整数，输出其中较大的数字。
# 2 输入三个整数， 求平均值和总和。
# 3 输入自己姓名和班级，然后输出。
# 这次三个作业重点就是让同学们理解两点：第一 python的编码风格（请看书本19页），第二 输入 输出 基本格式
# 附1：作业不用写在本子上，每个同学在自己的电脑上新建python文件夹（命名python）=》
# 再建子文件夹（命名chapter1） => 第一个程序文件命名exp_1（扩展名会自动添加）。以后就按照章节做练习。

# 1 输入两个整数，输出其中较大的数字。
print("输入两个整数，输出其中较大的数字。")
x = int(input("Enter the digit: "))
y = int(input("Enter the digit: "))
if x > y:
    print(x)
elif x < y:
    print(y)

# 2 输入三个整数， 求平均值和总和。
print("输入三个整数， 求平均值和总和。")
a = int(input("输入第一个数字："))
b = int(input("输入第二个数字："))
c = int(input("输入第三个数字："))
print("总和", a + b + c, "平均数", (a + b + c) / 3)

# 3 输入自己姓名和班级，然后输出。
print("输入自己姓名和班级，然后输出。")
name = input("输入自己姓名：")
classname = input("输入自己班级：")
print("姓名：", name, "班级：", classname)
