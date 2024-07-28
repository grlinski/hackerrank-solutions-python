

# HR Deque
# https://www.hackerrank.com/challenges/py-collections-deque/problem
from collections import deque

commands = {'append':1,'appendleft':2,'pop':3,'popleft':4}
d = deque()

t = int(input())
for i in range(t):
    a = input().split()
    if len(a) ==1:
        if a[0] == 'pop':
            d.pop()
        else:
            d.popleft()
    else:
        if a[0] == 'append':
            d.append(a[1])
        else:
            d.appendleft(a[1])


for i in d:
    print(i,end=' ')















