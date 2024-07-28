

# The Grid Search
# https://www.hackerrank.com/challenges/the-grid-search/problem


def printGrid(x):
    for i in x:
        print(i)




def createGrid(grid,r,c,startC,startR):
    newgrid = []
    startC-=1
    print('ROW',startR,startR+r)
    print('COL',startC,startC+c)

    for i in range(startR,startR+r):
        y = ''
        z = ''
        for j in range(startC,startC+c):
            x = str(grid[i])
            y = y+ x[1:-1]
            z+=y[j]
        newgrid.append(int(z))

    return newgrid


def compareGrids(ng,item):
    if len(ng)!= len(item):
        return False

    for i in range(0,len(ng)):
        print(str(ng[i]), str(item[i]))



def finder(grid,item,itemR,itemC):

    itemhold = str(item[0])
    item1 = itemhold[1:-1]
    for i in range(0,len(grid)):
        stringer = str(grid[i])
        if item1 in stringer:
            index = stringer.find(item1)
            ng = createGrid(grid,r,c,index,i)
            compareGrids(ng,item)














cases = int(input())

for i in range(cases):
    r,c = map(int, input().split(' '))
    grid =[]
    for j in range(r):
        x = list(map(int, input().strip().split(' ')))
        grid.append(x)

    r, c = map(int, input().split(' '))
    item = []
    for j in range(r):
        x = list(map(int, input().strip().split(' ')))
        item.append(x)

    finder(grid,item,r,c)
























