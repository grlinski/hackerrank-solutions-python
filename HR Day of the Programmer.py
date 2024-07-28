
# https://www.hackerrank.com/challenges/day-of-the-programmer/problem
# Day of the Programmer

# Leap Years are divisible by 400, 4 but not 100. Unless divisible by 400.

# Find the date of the 256th day according to the Russian calendar by year
# They switched from Julian to Gregorian on 1918 Jan 31st.

# Output is dd.mm.yyyy

import datetime, random



def date_gen():
    date = random.randint(1700,2600)
    return date

# 12.09.
# 13.09.

def dofp(x):

    if x == 1918:
        return '26:09:1918'
    elif ((x < 1918 and x%4==0) or (x%4 == 0 and x%100 != 0) or x%400 == 0):
        return '12.09.'+str(x)
    else:
        return '13.09.'+str(x)


#y = date_gen()
print(dofp(y))






"""
def solve(x):
    LY = False
    #Leap Year?
    if x%400 == 0:
        LY = True
    elif x%4 == 0 and x%100!=0:
        LY = True
    if x == 1918:
        return '26.09.1918'
    elif x < 1918 or LY:
        return '12.09.'+str(x)
    else:
        return '13.09.'+str(x)


"""




