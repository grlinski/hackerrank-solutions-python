


# https://www.hackerrank.com/challenges/picking-numbers/problem
# Picking Numbers


"""

Input
Array Size
Array

6
1 2 2 3 1 2

"""



n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
q = []

for i in range(0,max(a)+1):
    q.append(0)

for i in a:
    q[i]+=1
#print(q)

topmost=0

for i in range(0,len(q)-1):
    x = q[i]
    y = q[i+1]
    z = x+y
    topmost = max(topmost,z)

print(topmost)























