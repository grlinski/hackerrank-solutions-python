

# Strange Counter
# https://www.hackerrank.com/challenges/strange-code/problem




def findTime(t,c):
    # Rough Pass
    pass






"""
Start Time starts at 1 initially
Next time = the previous time and the initial value
Value double each time, or is 2+ the inital time value.

Time, Value Top
1,3
4,6
10,12
22,24
46,48
94,96

Time, Value Bottom
3,1
9,1
21,1



"""


x = int(input())

r1 = -1
r2 = -1
rv = -1
time = 1
value = 3
# Rough Search
for i in range(40):
    #print(time,value)
    newvalue = value*2
    newtime=newvalue-2
    if x >= time and x < newtime:
        #print(time,newtime-1)
        r1 = time
        r2 = newtime-1
        rv = value
        #print(value)
        break
    else:
        time = newtime
        value = newvalue

#print(r1,r2)
#print(rv)
#print(x)
diff = abs(x-r1)
answer = value-diff
print(answer)





