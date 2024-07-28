

# A Chessboard Game
# https://www.hackerrank.com/challenges/a-chessboard-game-1/problem

import math


def getDistance(x,y):
    xn = x**2
    yn = y**2
    xy = xn+yn
    d = math.sqrt(xy)
    return d



def playGame(x,y):
    player = 1
    # MOVES
    """
    u2l1
    l2u1
    l2d1
    u2r1
    """
    #Always Pick move furthest away from end zone
    #Or pick move that will move into end zone.
    endzone = [[0,0],[0,1],[1,0],[1,1]]
    curPos = [x,y]

    while curPos not in endzone:

        possibleMoves = [[x-2,y+1],[x-2,y-1],[x+1,y-2],[x-1,y-2]]
        distance = ['x','x','x','x']
        posMoves = 0
        mini = 1000
        for i in (possibleMoves):
            a = i[0]
            b = i[1]

            if [a,b] in endzone:
                return player
            elif a < 0 or a > 15 or b < 0 or b > 15:
                distance[posMoves] = 1000
            else:
                distance[posMoves] = getDistance(a,b)
                mini = min(mini,getDistance(a,b))
            posMoves+=1
        posMoves = 0
        for i in range(4):
            if distance[i] == mini:
                x = possibleMoves[i][0]
                y = possibleMoves[i][1]

        curPos = [x,y]
        print(player,x,y)
        if player ==1:
            player = 2
        else:
            player = 1












t = int(input())
for i in range(t):
    a,b = map(int, input().split(' '))
    ans = playGame(a,b)
    if ans ==1:
        print('FIRST')
    else:
        print('SECOND')















