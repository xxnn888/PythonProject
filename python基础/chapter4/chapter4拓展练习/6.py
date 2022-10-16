import calendar
Datetime = input("please input a datatime (such as:201012): \n")
if len(Datetime)!=6:
    print("-- input error , please input 6-bit digital --")
    Datetime = input("please input again: \n")
Years = int(Datetime[0:4])
Month = int(Datetime[4:6])
monthRange = calendar.monthrange(Years,Month)
print("%d年%d月有%d天" % (Years,Month,monthRange[1]))