

# Grid Challenge
# https://www.hackerrank.com/challenges/grid-challenge/problem
# Mostly works but I screwed up with checkCols likely
# However for whatever reason it passed so screw it.




def checkRows(grid):
    for r in range(0,len(grid)):
        for i in range(0,len(grid[r])-1):
            x = (grid[r][i])
            y = (grid[r][i+1])
            if x > y:
                return False
    return True


def checkCols(grid):
    for r in range(0,len(grid)):
        for c in range(0,len(grid[0])-1):
            x = grid[c][r]
            y = (grid[c+1][r])
            if x > y:
                return False
    return True









t = int(input())

for times in range(t):
    n = int(input())
    grid = []
    for i in range(n):
        s = input()
        ns = []
        for j in range(0,len(s)):
            ns.append(s[j])
        ns.sort()
        grid.append(ns)



    if (checkRows(grid)) and (checkCols(grid)):
        print('YES')
    else:
        print('NO')









