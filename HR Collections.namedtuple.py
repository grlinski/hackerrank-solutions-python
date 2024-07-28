

#  Collections.namedtuple()
# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem


# Screw Named Tuple



t = int(input())
fields = input().split()
pos = 0
for i in range(0,len(fields)):
    if fields[i]=='MARKS':
        pos = i

total = 0
for i in range(t):
    s = input().split()

    total += int(s[pos])


print(total/t)














