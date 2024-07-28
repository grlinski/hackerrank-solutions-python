# The Bomberman Game Mk5
# https://www.hackerrank.com/challenges/bomber-man/problem
"""
Steps
Inital Setup
One second of nothing, only in the start, since no bombs would go off.
Plants bombs in empty cells
Inital Bombs explode, destroying things in a cross formation

Then things loop until the end
Plant bombs
Bombs explode after 3 seconds.

Create an id config for the grid state.
Either the entire thing or some long string
Maybe something like
abc,e
2a4b2eX3e1b2eX and so on
a = inital bomb placement
b = bomb after one second
c = bomb after 3 seconds
e = empty.
X = new line


"""
# COMMON FUNCTIONS
########################

def printGrid(grid):
    for i in grid:
        print(i)

def copyGrid(grid):
    newGrid = []
    for i in range(0,len(grid)):
        temp = []
        for j in range(0,len(grid[0])):
            x = grid[i][j]
            temp.append(x)
        newGrid.append(temp)
    return newGrid

def answerGrid(grid):
    ans = []
    for i in range(0, len(grid)):
        s = ''
        for j in range(0, len(grid[0])):
            x = grid[i][j]
            if x!= '.':
                s+='O'
            else:
                s+='.'
        ans.append(s)
    for i in ans:
        print(i)











r,c,endTime = map(int, input().split(' '))

grid = []
for i in range(0,r):
    temp = []
    x = input()
    for j in range(0,c):
        q = x[j]
        if q == 'O':
            q = 2


        temp.append(q)
    grid.append(temp)


printGrid(grid)





















