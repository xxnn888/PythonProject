# def outer():
#     def inner():
#         print(max(1, 10))
#
#     inner()
# outer()

import os

filename = 'file\\'
if not os.path.exists(filename):
    os.mkdir(filename)


def stu_in():
    name = input("name:")
    maths = float(input("输入数学成绩:"))
    chin = float(input("语文:"))
    return {"name": name, "maths": maths, "chin": chin}


def stu_sum(stud):
    return stud["maths"] + stud["chin"]


def stu_avg(stud):
    return (stud["maths"] + stud["chin"]) / 2


def main():
    student1 = stu_in()
    print("总分是：", stu_sum(student1))
    print("平均分是：", stu_avg(student1))
    with open(filename + title , mode='wb') as f:
        f.write(music_content)


main()
