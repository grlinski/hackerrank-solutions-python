# Library Fine Hacker Rank
# So we take in two dates in the form of day, month, year.
# The first date is the return date, the second is the due date.



# 15 dollars per day, within the month
# 500 dollars per month
# 10 000 dollars if past the year and that is the cap


# Return Date
d1,m1,y1 = 9,3,2016
# Expected Date
d2,m2,y2 = 6,6,2015


#Differences
dd = d1 - d2
md = m1 - m2
yd = y1 - y2

fine = 0
months =0

if yd > 1:
    fine = 10000
elif yd > -1:
    months = yd*12+md


print(months)


#Answer
print(fine)
print(dd,md,yd)

""" 

Extraneous Work

On and off types for year/month/day
111
110
101
100
011
010
001
000

"""





























