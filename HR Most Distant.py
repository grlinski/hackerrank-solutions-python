


# More Distant
# https://www.hackerrank.com/challenges/most-distant/problem

import math

def solve(coordinates):
    rightmost = 0
    leftmost = 0
    topmost = 0
    downmost = 0
    ans = 0

    #print(coordinates[0])

    for i in coordinates:
        x = i[0]
        y = i[1]
        #print(x,y)

        rightmost = max(i[0],rightmost)
        leftmost = min(i[0], leftmost)
        topmost = max(i[1], topmost)
        downmost = min(i[1], downmost)



    # 6 Different Distances
    #Left to Right, Left to top, left to down
    # Top to Down, Right to Down, Right to Top

    # Left to Right
    lr = abs(rightmost-leftmost)

    #Top to Down
    td = abs(topmost - downmost)

    # Left to Top
    lt = math.sqrt(leftmost**2+topmost**2)

    # Left to Down
    ld = math.sqrt(leftmost ** 2 + downmost ** 2)

    # Right to Top
    rt = math.sqrt(rightmost ** 2 + topmost ** 2)

    # Right to Down
    rd = math.sqrt(rightmost ** 2 + downmost ** 2)

    print(max(lr,td,lt,ld,rt,rd))




t = int(input())

coord = []
for i in range (t):
    q = []
    x,y = map(int,input().split(' '))
    q.append(x)
    q.append(y)
    coord.append(q)

solve(coord)

















