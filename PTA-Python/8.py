# year, month， day均为int
import datetime

a = (input())
d1 = datetime.date(int(a[0:4]), int(a[4:6]), int(a[-2:]))
d2 = datetime.date(2022, 3, 19)
if int(a) > 20220319:
    print("hai you", (d1 - d2).days, "tian")
elif int(a) < 20220319:
    print("guo qv", (d2 - d1).days, "tian")
else:
    print("jiu shi jin tian!")
