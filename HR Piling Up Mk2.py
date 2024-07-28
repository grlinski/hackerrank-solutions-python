

# Piling Up
# https://www.hackerrank.com/challenges/piling-up/problem

"""
Pop is righthand side/the end



"""


from collections import deque



def piler(cubes):
    s = 0
    e = len(cubes)-1
    prev = 0
    counter = 1
    while True:
        a = cubes[0]
        b = cubes[-1]
        #print('Counter',counter)
        counter+=1

        if ((a > prev and a > b) or (b > a and b > prev)) and (prev!=0):
            #print('Didn\'t Work')
            #print(cubes)
            #print(prev)
            return 'No'
        elif a >=b:
            prev = cubes.popleft()
            #print('Pop A',a)
        else:
            prev = cubes.pop()
            #print('Pop B', b)
        #print(cubes)
        if len(cubes) == 0:
            return 'Yes'
    return 'Yes'



t = int(input())

for i in range(t):
    n = int(input())
    #cubes = list(map(int, input().strip().split(' ')))
    cubes = deque(map(int, input().strip().split()))


    if n == 1 or n == 2:
        print('Yes')
    elif n == 3:
        if cubes[1] > cubes[0] and cubes[1] > cubes[2]:
            print('No')
        else:
            print('Yes')
    else:
        print(piler(cubes))








"""

Problems:

3
11
1 10 10 1
11
2 1 5 5 2 2
11
2 1 5 2 2


1
11
10 9 8 7 6 5 4 3 2 100 1110 90 40 1 2 9 10 2 1999 2000 2101 13109 1 2 3 4 5 6 7 8 9 10


1
11
100 100 100 100 100 100 100 100 100

"""







