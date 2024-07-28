


# Calendar Module
# https://www.hackerrank.com/challenges/calendar-module/problem

# Used datetime instead


import datetime



m,d,y = map(int, input().split(' '))

date1 = datetime.datetime(y,m,d)
# This is the date in Y:M:D:H:M:S:MilS: time

# Making the Data More Readable
x = (date1.strftime('%A'))
y = x.upper()
print(y)










