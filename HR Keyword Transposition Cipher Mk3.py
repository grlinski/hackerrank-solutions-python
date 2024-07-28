
# Keyword Transposition Cipher Mk3
# https://www.hackerrank.com/challenges/keyword-transposition-cipher/problem
"""
So I didn't fully read the question
The segement at the end is what I need to translate
I start with an alphabet grid.




"""
def printGrid(grid):
    for i in grid:
        print(i)


def flipGrid(grid):
    row = len(grid)
    col = len(grid[0])
    newGrid = blankGrid(col,row)
    for i in range(0,row):
        for j in range(0,col):
            newGrid[j][i] = grid[i][j]
    return(newGrid)


def blankGrid(row,col):
    grid = []
    for i in range(0,row):
        temp = []
        for j in range(0,col):
            temp.append('0')
        grid.append(temp)
    return grid

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

def alphabetGrid(keyword,order):

    keywordList = []
    for i in keyword:
        if i in keywordList:
            pass
        else:
            keywordList.append(i)

    abGrid = []
    col = len(keywordList)
    row = 26//col
    if 26%col >0:
        row+=1
    abGrid = blankGrid(row,col)

    for i in range(0,26):
        letter = chr(65+i)
        if letter in keywordList:
            pass
        else:
            keywordList.append(letter)

    pos =0
    for i in range(0,row):
        for j in range(col):
            abGrid[i][j] = keywordList[pos]
            pos+=1
            if pos ==len(keywordList):
                break


    newGrid = blankGrid(row,col)

    for i in range(0,len(abGrid)):
        for j in range(0,len(abGrid[0])):
            newPos = order[j]
            newGrid[i][newPos] = abGrid[i][j]

    newGrid = flipGrid(newGrid)

    transposeAlpha = []
    alpha = []
    for i in range(0,len(newGrid)):
        for j in range(0,len(newGrid[0])):
            cur = newGrid[i][j]
            if cur == '0':
                pass
            else:
                transposeAlpha.append(cur)

    for i in range(0,len(transposeAlpha)):
        letter = chr(i+65)
        alpha.append(letter)


    translator = {}
    for i in range(0,len(transposeAlpha)):
        x = transposeAlpha[i]
        y = alpha[i]
        translator[x] = y
    return translator



def translate(s,translator):
    ans = ''
    singleLine = ''
    for i in s:
        singleLine+=i
        singleLine+=' '


    for i in singleLine:
        if i ==' ':
            ans+=i
        else:
            ans+=translator[i]
    print(ans[:-1])


times = int(input())
for i in range(times):
    keyword = input()
    s = input().split(' ')
    order,fw = alphabetize(keyword)
    translator = alphabetGrid(keyword,order)
    translate(s,translator)






















