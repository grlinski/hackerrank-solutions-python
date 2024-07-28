

# The Grid Search
# https://www.hackerrank.com/challenges/the-grid-search/problem

"""
This time store everything as a string in the list
Try to remove all brackets before storing
This is just to make everything far less of a headache.
Otherwise everything else in the original program seems fine.

"""

def printGrid(x):
    for i in x:
        print(i)



def createGrid(grid,itemR,itemC,rowS,colS):
    # Grid is what I'm copying the newgrid from
    # ItemR is how many rows the new grid is
    # ItemC is how many cols the new grid is
    # rowS and colS is where I start from in grid

    newgrid = []
    for i in range(itemR):
        x = ''
        for j in range(itemC):
            try:
                x +=(grid[rowS+i][colS+j])
            except:
                return False,newgrid
        newgrid.append(x)

    #printGrid(newgrid)

    return(True,newgrid)



def compareGrids(newgrid,item):

    if newgrid == item:
        return True
    else:
        return False




def finder(grid,item,itemR,itemC):
    item1 = str(item[0])



    for i in range(0,len(grid)):
        for j in range(0,len(grid[0])):
            stringer = grid[i][j:j+itemC]
            if stringer == item1:

                #NOTE i is the row, downwards
                # and index is the column

                #print(i,j)
                #print(stringer)
                # The newly created grid function
                # itemR is how many rows the item grid is, itemC how many cols
                # rowS and colS are where the first part of item is found in the main grid
                # So I try to create a new grid from the ori grid using specs from item
                gridReturned,newgrid = createGrid(grid,itemR,itemC,i,j)
                if gridReturned:
                    same = compareGrids(newgrid,item)
                    if same:
                        return('YES')

    return ('NO')


cases = int(input())

for i in range(cases):
    r,c = map(int, input().split(' '))
    grid =[]
    for j in range(r):
        x = input()
        grid.append(x)

    r, c = map(int, input().split(' '))
    item = []
    for j in range(r):
        x = input()
        item.append(x)

    ans = finder(grid,item,r,c)
    print(ans)



























