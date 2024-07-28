

# Piling Up
# https://www.hackerrank.com/challenges/piling-up/problem

def piler(cubes):
    back = len(cubes)-1
    start = 0

    lastpiled = 0

    while True:
        x = cubes[start]
        y = cubes[back]

        #print(x,y)

        if start == back:
            #print('Overlap')
            return 'Yes'


        if (lastpiled < x or lastpiled <  y) and lastpiled !=0:
            return 'No'


        if x == y:
            start+=1
            back-=1
            lastpiled = x
        elif x > y:
            lastpiled = x
            start+=1
        elif y > x:
            lastpiled = y
            back-=1

    return 'Yes'




t = int(input())

for i in range(t):
    n = int(input())
    cubes = list(map(int, input().strip().split(' ')))
    if n == 1 or n == 2:
        print('Yes')
    else:
        print(piler(cubes))



















