
# The Bomberman Game Mk4
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


Replace Bombs with timers.








This probably works for all cases
Just not fast enough
How to streamline it?

In all likelihood the grid will cycle between states
Keep a time index along with an id config
Then I can extrapolate when n is very large.
If the id config ever is the same again, then I know for certain there is a pattern
id config??
likely only need a few values, maybe the diagnal
Or top row and right column??
However may give false positives.

maybe 3 ids
top row, right col
Top left to bottom right diag.
Store Ids in dict along with grid pattern
Then find which one will be at time n




"""


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




def plantBombs(grid):
    for i in range(0,len(grid)):
        for j in range(0,len(grid[0])):
            x = grid[i][j]
            if x == '.':
                pass

def firstSecond(grid):
    pass


def nextStep(grid):
    """
    3,2 countdown
    1 explodes in cross formation
    . gets replaced with 3s


    """
    for i in range(0,len(grid)):
        for j in range(0,len(grid[0])):
            x = grid[i][j]
            if x == '.':
                grid[i][j] = 3
            elif x == 3:
                grid[i][j] = 2
            elif x == 2:
                grid[i][j] = 1
            elif x == 1:
                grid[i][j] = 'X'

                if i-1!=-1:
                    if grid[i-1][j]!=1:
                        grid[i-1][j] = 'X'

                if i + 1 != len(grid):
                    if grid[i + 1][j] != 1:
                        grid[i+1][j] = 'X'

                if j + 1 != len(grid[0]):
                    if grid[i][j+1] != 1:
                        grid[i][j+1] = 'X'

                if j - 1 != -1:
                    if grid[i][j-1] != 1:
                        grid[i][j-1] = 'X'

    # IDs
    topRow = ''
    leftCol = ''
    diag = ''

    for i in range(0,len(grid)):
        for j in range(0,len(grid[0])):
            x = grid[i][j]
            if x == 'X':
                grid[i][j] = '.'
            if i==0:
                topRow+=str(grid[i][j])
            if j==0:
                topRow+=str(grid[i][j])
            if i==j:
                topRow+=str(grid[i][j])

    id = topRow+leftCol+diag

    return grid,id




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


patterns = {}
#print('...........................................')
#printGrid(grid)
usePatterns = True
if endTime > 50:
    endTimeMax50 = 50
else:
    endTimeMax50 = endTime
    usePatterns = False

for i in range(0,endTimeMax50-1):
    grid,id = nextStep(grid)
    #print('...........................................')
    #printGrid(grid)


    if id in patterns:
        pass
    else:
        cGrid = []
        cGrid = copyGrid(grid)
        patterns[id] = cGrid

#answerGrid(grid)
if usePatterns == False:
    answerGrid(grid)

else:
    #"Correct Answer"

    # PATTERN SECTION
    ###################
    #print('PATTERN SECTION !!!!!!!!!!!!!!!!!!!!!!!!!!')

    totalP = 0
    numberingPatterns = []
    endLoop = False
    counter = 0


    for i in patterns:
        #print(i)
        #printGrid(patterns[i])
        if i in numberingPatterns:
            endLoop = True
            break
        else:
            numberingPatterns.append(i)
        totalP+=1
        counter += 1

    rem = endTime%counter
    rem+=1

    x = (numberingPatterns[rem])
    y = patterns[x]
    #print(x)
    #print(y)
    answerGrid(y)
    #print(rem)
    #print(numberingPatterns)















