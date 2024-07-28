
# HR Crossword Puzzle
# https://www.hackerrank.com/challenges/crossword-puzzle/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=recursion-backtracking
"""

Solved
One of my main problems was that I couldn't get a section to loop properly
It turns out I used if rather than while
This caused much confusion
Other than that it was somewhat challenging, yet very doable.
Small things at a time.
I should bother with classes at some point
Instead of a list of coordinates, I could create a specific class that stores all that info for me in a variable.




Probably Should Restart
I really need to rework the coordinate system.
Maybe implement it earlier.
Also Keep a list of Used words
So I can delete those from the coordinate system.
Also there seems to be a problem before in def coordinateDictionary
I'm missing a coordinate, specifically 3,1 length 7
For the ANDAMA testcase 6




"""










###################
# Common Functions
def printAnswerGrid(grid):
    for i in grid:
        temp = ''
        for j in i:
            temp +=j
        print(temp)

def flipGrid(grid):
    flippedGrid = []
    for i in range(0,len(grid)):
        temp = []
        for j in range(len(grid[i])):
            temp.append(grid[j][i])
        flippedGrid.append(temp)
    return flippedGrid

def copyGrid(grid):
    cg = []
    for i in range(0,len(grid)):
        temp = []
        for j in range(len(grid[i])):
            temp.append(grid[i][j])
        cg.append(temp)
    return cg

def printGrid(grid):
    for i in grid:
        print(i)
    print()
############################################


def crosswordSolver(grid,coordA,coordD,across,down,words):
    # Places words of a single length into the grid
    grid,coordA,coordD,across,down,words = oneFit(grid,coordA,coordD,across,down,words)
    wordLengths = wordLengthFinder(words)

    cd = coordinateDictionary(coordA,coordD,words,wordLengths)
    ca = True

    while ca == True:
        cd,grid,ca = refineCoordinateDictionary(cd,grid)



    printAnswerGrid(grid)
    #print(cd)

# Removes Coordinate Word Candidates That Do Not Fit into Grid
# If there is only one Candidate it Places it In Via placeWord

def refineCoordinateDictionary(cd,grid):
    cycleAgain = False
    usedWords = []
    for coord in cd:
        if cd[coord] == []:
            cycleAgain = True
            break

        fullKey = coord
        cLength = int(coord[0])
        cDirect = str(coord[1])
        x = int(coord[2])
        y = int(coord[3])
        cwords = cd[coord]
        if len(cwords) == 1:
            coord = [x,y]
            word = cwords[0]
            grid = placeWord(grid,coord,cDirect,word)
            usedWords.append(word)
            cycleAgain = True
            cd[fullKey] = []

        else:
            for w in cwords:


                fit = couldWordFit(w,grid,[x,y],cDirect)
                if fit == False:
                    cycleAgain = True
                    cwords.remove(w)
                    cd[coord] = cwords

    listOfKeys = []
    listOfValues = []
    for i in cd:
        if cd[i] == []:
            pass
        else:
            listOfKeys.append(i)
            listOfValues.append(cd[i])
    nCD = {}


    for i in range(0, len(listOfKeys)):
        nCD[listOfKeys[i]] = listOfValues[i]

    return nCD,grid,cycleAgain



# Returns True or False if a word Could fit in a specific Coordinate and Direction
def couldWordFit(word,grid,coord,direction):
    # Across
    if direction == 'a':
        wStart = 0
        x = coord[0]
        y = coord[1]
        length = len(word)
        for i in range(0, len(grid)):
            if wStart == length:
                break
            for j in range(0, len(grid[i])):
                if i == x and j == y:
                    if grid[i][j] == word[wStart] or grid[i][j] == '-':
                        pass
                    else:
                        return False
                    wStart += 1
                    y += 1
                    if wStart == length:
                        break
    # Down
    elif direction == 'd':
        wStart = 0
        x = coord[0]
        y = coord[1]
        length = len(word)
        for i in range(0, len(grid)):
            if wStart == length:
                break
            for j in range(0, len(grid[i])):
                if i == x and j == y:
                    if grid[i][j] == word[wStart] or grid[i][j] == '-':
                        pass
                    else:
                        return False
                    wStart += 1
                    x += 1
                    if wStart == length:
                        break
    return True




def coordinateDictionary(coordA,coordD,words,wordLengths):
    cd = {}
    # Across
    for i in coordA:
        for j in coordA[i]:
            ent = [i,'a',j[0],j[1]]
            tup = tuple(ent)
            cd[tup] = []
            for j in words:
                if len(j) == i:
                    cd[tup].append(j)

    for i in coordD:
        for j in coordD[i]:
            ent = [i,'d',j[0],j[1]]
            tup = tuple(ent)
            cd[tup] = []
            for j in words:
                if len(j) == i:
                    cd[tup].append(j)

    return cd


def oneFit(grid,coordA,coordD,across,down,words):
    onlyOneLength = []
    allLengths = across+down
    for i in range(0,len(allLengths)):
        newList = allLengths[:i]+allLengths[i+1:]
        if allLengths[i] in newList:
            pass
        else:
            onlyOneLength.append(allLengths[i])
    lengthDict = {}
    for i in words:
        leng = len(i)
        if leng in onlyOneLength:
            lengthDict[leng] = i

    for i in onlyOneLength:
        if i in coordA:
            w = lengthDict[i]
            coord = coordA[i][0]
            grid = placeWord(grid,coord,'a',w)
            words.remove(w)
            across.remove(i)
            del coordA[i]
        elif i in coordD:
            w = lengthDict[i]
            coord = coordD[i][0]
            grid = placeWord(grid,coord,'d',w)
            words.remove(w)
            down.remove(i)
            del coordD[i]

    return grid,coordA,coordD,across,down,words





def placeWord(grid,coord,direction,word):
    # Across
    if direction == 'a':
        wStart = 0
        x = coord[0]
        y = coord[1]
        length = len(word)
        for i in range(0,len(grid)):
            if wStart == length:
                break
            for j in range(0,len(grid[i])):
                if i == x and j == y:
                    grid[i][j] = word[wStart]
                    wStart+=1
                    y+=1
                    if wStart == length:
                        break
    # Down
    elif direction == 'd':
        wStart = 0
        x = coord[0]
        y = coord[1]
        length = len(word)


        for i in range(0, len(grid)):
            if wStart == length:
                break
            for j in range(0, len(grid[i])):
                if i == x and j == y:

                    grid[i][j] = word[wStart]
                    wStart += 1
                    x += 1
                    if wStart == length:
                        break
    return grid



def wordLengthFinder(words):
    wL = {}
    for i in words:
        length = len(i)
        if length in wL:
            wL[length].append(i)
        else:
            wL[length] = [i]
    return wL

def blankLengthFinder(grid):
    flippedGrid = flipGrid(grid)
    across = []
    down = []
    coordA = {}
    coordD = {}

    for i in range(len(grid)):
        startA = 0
        startD = 0
        for j in range(len(grid[i])):
            curA = grid[i][j]
            curD = flippedGrid[i][j]
            if curA == '-':
                startA +=1
                ax = i
                ay = j

            elif curA == '+' and startA > 1:
                across.append(startA)
                if startA in coordA:
                    coordA[startA].append([ax,ay-startA+1])
                else:
                    coordA[startA] = [[ax,ay-startA+1]]
                startA = 0
            elif curA == '+':
                startA = 0
            if curD == '-':
                startD += 1
                dx = i
                dy = j
            elif curD == '+' and startD > 1:
                down.append(startD)
                if startD in coordD:
                    coordD[startD].append([dy-startD+1, dx])
                else:
                    coordD[startD] = [[dy-startD+1, dx]]
                startD = 0
            elif curD == '+':
                startD = 0

        if startA > 1:
            across.append(startA)
            if startA in coordA:
                coordA[startA].append([ax, ay - startA + 1])
            else:
                coordA[startA] = [[ax, ay - startA + 1]]
        if startD > 1:
            down.append(startD)
            if startD in coordD:
                coordD[startD].append([dy-startD+1, dx])
            else:
                coordD[startD] = [[dy-startD+1, dx]]

    return coordA,coordD,across,down







def flowControl(grid,words):
    #wL = wordLengthFinder(words)
    coordA,coordD,across,down = blankLengthFinder(grid)
    crosswordSolver(grid,coordA,coordD,across,down,words)



grid = []
for i in range(0,10):
    x = input()
    temp = []
    for j in x:
        temp.append(j)
    grid.append(temp)

words = input().split(';')


flowControl(grid,words)
#printGrid(grid)
#copyG = copyGrid(grid)
#fG = flipGrid(grid)
#printGrid(copyG)
#printGrid(fG)



