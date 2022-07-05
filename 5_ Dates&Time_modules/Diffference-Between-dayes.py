from datetime import datetime, date

t1 = date(year = 2021, month = 8, day = 8)
t2 = date(year = 2001, month = 8, day = 8)


t3 = t1 - t2
print("t3 =", t3)
# print(dir(date))