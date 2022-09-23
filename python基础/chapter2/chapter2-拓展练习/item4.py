import math

b = -10
a = 1
c = 16
d = b ** 2 - 4 * a * c
if d == 0:
    print("只有一个解，{}".format(-b / 2 * a))
elif d < 0:
    print("没有实数解。")
elif d > 0:
    x = math.sqrt(d)
    print("有两点实数根", (-(b + x) / 2 * a), (-(b - x) / 2 * a))
