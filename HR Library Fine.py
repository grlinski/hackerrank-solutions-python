
# Library Fine
#


# Completed

import datetime

rDay,rMonth,rYear = map(int, input().split(' '))
dDay,dMonth,dYear = map(int, input().split(' '))


diffDay = rDay-dDay
diffMonth = rMonth-dMonth
diffYear = rYear-dYear

total = 0
if diffYear > 0:
    total = 10000
elif diffYear <0:
    total = 0
elif diffMonth > 0:
    total = diffMonth*500
elif diffMonth < 0:
    total = 0
elif diffDay > 0:
    total = diffDay*15

print(total)







