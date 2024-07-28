
# Find the Point
# https://www.hackerrank.com/challenges/find-point/problem


"""
Basically we take in 2 coordinates, say 1,1 and 2,2
Then we find a third point, basically a reflection on the second point
So our reflection would be at 3,3





2
0 0 1 1
1 1 2 2



"""


import math

def reflect(x1,y1,x2,y2):
    distance = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    xdif = abs(x2-x1)
    ydif = abs(y2-y1)

    if x1 < x2:
        xr = x2+xdif
    else:
        xr = x2-xdif
    if y1 < y2:
        yr = y2+ydif
    else:
        yr = y2-ydif

    print(xr, yr)



n = int(input())
list2 = []

while True:
    list1 = []
    try:
        a1,b1,c1,d1 = input().split()
    except:
        break
    a, b, c, d = int(a1), int(b1), int(c1), int(d1)
    list1.append(a)
    list1.append(b)
    list1.append(c)
    list1.append(d)
    list2.append(list1)

for i in list2:
    reflect(i[0],i[1],i[2],i[3])

















