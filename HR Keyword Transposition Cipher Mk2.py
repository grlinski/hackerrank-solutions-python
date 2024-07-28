
# Keyword Transposition Cipher
# https://www.hackerrank.com/challenges/keyword-transposition-cipher/problem

def printGrid(grid):
    for i in grid:
        print(i)
def blankGrid(row,col):
    grid = []
    for i in range(0,row):
        temp = []
        for j in range(0,col):
            temp.append('0')
        grid.append(temp)
    return grid

# Sorts an item Alphabetically and returns a dict
# Old Pos -> New Pos
# Key -> Value
def alphabetize(x):
    list1 = []
    list2 = []
    for i in x:
        list1.append(i)
        if i in list2:
            pass
        else:
            list2.append(i)
    list1 = list(set(list1))
    list1.sort()
    dictab = {}
    dictba = {}
    s = ''
    for i in list1:
        s+=i
    for i in range(0,len(list2)):
        a = list2[i]
        for j in range(0,len(list2)):
            b = list1[j]
            if a==b:
                dictab[i] = j
                dictba[j] = i
    fw = ''
    for i in list1:
        fw+=i
    return dictab,fw

# Fills in the Grid and Sorts by list1
# Also adds in the Keyword to the first row
def fillGrid(grid,list1,fw):
    col = len(list1[1])
    row = len(list1)
    for i in range(row):
        for j in range(col):
            try:
                letter = list1[i][j]
            except:
                break
            newPos = order[j]
            grid[i][newPos] = letter
    firstRow = []
    for i in fw:
        firstRow.append(i)
    grid = [firstRow]+grid
    return grid


def flipGrid(grid):
    row = len(grid)
    col = len(grid[0])
    newGrid = blankGrid(col,row)

    for i in range(0,row):
        for j in range(0,col):
            newGrid[j][i] = grid[i][j]
    printGrid(newGrid)




times = int(input())
for i in range(times):
    keyword = input()
    s = input().split(' ')
    order,fw = alphabetize(keyword)
    grid = blankGrid(len(s),len(s[0]))
    grid = fillGrid(grid,s,fw)
    flipGrid(grid)





















