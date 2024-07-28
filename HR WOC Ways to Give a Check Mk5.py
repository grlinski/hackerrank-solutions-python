# Ways to Give a Check Mk5
"""

Didn't Pass the Test Cases

Went back and reread the question
minor changes
There are upwards of 4 pieces on the board
4 for each colour



Need to Account for other White Pieces
Can they check the king


Need to See If There is Something blocking my pawn from moving to the 0th row



"""

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1



# The original program works well so before I screw with it it's best to have the original somewhere else
# Works AFAICT, but now it needs to determine blocks
# If pieces interfere with the checks

# However luckily enough there will be at most 2 blocks
# Note if there are 2 pawns, one pawn may block the other
# So I need to store pawns as block, but remember to remove the current pawn as a block.

# Also May as Well Combing all types of promotions, ie Knights with Rooks,Queens and Bishops
# Note blocks don't interfere with Knights, only KQB.







#!/bin/python3

import sys



# Note I made some changes to their way of doing this problem
# First I didn't store the board as a list of lists, because it wasn't really needed
# Second the top row to me is row 0, in their version it is row 8
# Again this just makes things easier for me and doesn't change anything







# MK2 !!!!!!!!!!!!!!!!!!!!!!!!!!! Look Here
# Step 1 add pawns to block list
# Step 2 determine how a block will affect QRB moves
# Note Knights aren't affected.
"""
Rooks are stopped if the block is between it and the king
also need to create a block list without the pawn
Since there are max two pawns maybe two lists and swap between them




"""






def waysToGiveACheck(board):
    # Change board back into a list of lists
    boardlist = []
    for i in board:
        for j in i:
            boardlist.append(j)
    #print(boardlist)


    # For My Pawns All I care about is row1, so I only have it's col position
    pawns = []
    # Everything but my pawns and the black king are blocks
    # This is stored as a lists within lists, x y coordinates
    # At most two blocks, only 4 pieces on the board, min 1 pawn, 1 bking, 1 white king, possibly 1 other piece
    blocks = []
    location = []
    # The Singular Black King stored as two values, x and y
    bking = []
    # White Pieces, uppercase values
    whiteQ = []
    whiteB = []
    whiteR = []
    whiteK = []
    whiteN = []


    # Hits Where the Promoted Pieces Can Get to

    hitcount = 0

    # Where Is Everything?
    # Pawns, King, Blocks
    # Note most everything is stored as row,col
    # Except pawns which are just col
    for i in range(0,8):
        for j in range(0,8):
            if boardlist[i][j] == 'P':
                pawns.append(j)
                location = []
                location.append(i)
                location.append(j)
                blocks.append(location)
            elif boardlist[i][j] == 'Q':
                location = []
                location.append(i)
                location.append(j)
                whiteQ.append(location)
                location = []
                location.append(i)
                location.append(j)
                blocks.append(location)
            elif boardlist[i][j] == 'K':
                location = []
                location.append(i)
                location.append(j)
                whiteK.append(location)
                location = []
                location.append(i)
                location.append(j)
                blocks.append(location)
            elif boardlist[i][j] == 'N':
                location = []
                location.append(i)
                location.append(j)
                whiteN.append(location)
                location = []
                location.append(i)
                location.append(j)
                blocks.append(location)
            elif boardlist[i][j] == 'B':
                location = []
                location.append(i)
                location.append(j)
                whiteB.append(location)
                location = []
                location.append(i)
                location.append(j)
                blocks.append(location)
            elif boardlist[i][j] == 'R':
                location = []
                location.append(i)
                location.append(j)
                whiteR.append(location)
                location = []
                location.append(i)
                location.append(j)
                blocks.append(location)
            elif boardlist[i][j] == 'k':
                bking.append(i)
                bking.append(j)
            elif boardlist[i][j] != '#':
                location = []
                location.append(i)
                location.append(j)
                blocks.append(location)
    # Works Up to Here
    # Stored all positions


    # Case 1, no Pawns on Row 1, Therefore no ways to check
    # Nevermind, always at least one pawn


    print('Next Board')
    print(boardlist)
    print(pawns)
    print(bking)
    print(blocks)
    #Knight Hits, Not Affected By Blocks
    # Later Only count hits, no need to do more
    # Store Values in list, since we need to count each individual hit
    # A knight can only hit the king once so if we get a hit there's no point in continuing
    # Also no need to store the values for later, just keep hitcount
    for i in pawns:

        hit = True

        # Other Piece Hit
        ophit = False



        # New Block List
        # First Step is to Create a New List of Blocks without the Current Pawn
        # The Current Pawn is always in row 1
        # Note I realized I have been storing info as row, col not x,y
        # I'm going ot continue with row,col and hopefully it all works out


        # Check if there is something blocking the pawn from moving up
        # Note need to create an else statment for everything else.
        isitblocked = [0,i]
        if isitblocked in blocks:
            hit = False
            #print('Blocked')
        else:

            newblocks = blocks
            currentpawn = [1, i]
            newblocks.remove(currentpawn)



            # Knight Moves, if the Knight Hits Nothing Else Does
            # Checks if the Knight hits the King
            # Range for x 0 to 7,
            # Don't Worry About Blocks for Knight Moves

            left1d2 = [2,i - 1]
            left2d1 = [1,i - 2]
            right1d2 = [2,i + 1]
            righh2d1 = [1,i + 2]


            if left1d2 == bking:
                hitcount+=1
                print('KL1D2')
            elif left2d1 == bking:
                hitcount+=1
                print('KL2D1')
            elif right1d2 == bking:
                hitcount+=1
                print('KR1D2')
            elif righh2d1 == bking:
                hitcount+=1
                print('KR2D1')

            # Knight Hits Works AFAICT






            # When a Block Matters
            # Never for Knights
            # For Rooks
            # When the block col is between the rook and king
            # When the block row is between the rook and king

            # For bishops
            # When the block's absolute difference of coordinates is between the rook and king



            # Rook Hits, Add Queen and Bishop Later
            # If the Rook Hits the Queen Hits Too, same idea with the Bishop
            # Later add in blocks
            # I only care about the king in row zero or the same col
            # This is for queens and rooks thus +2

            # Check if the col is between the king and pawn

            if bking [0] == 0:
                for b in newblocks:
                    if b[1] > min(bking[1],i) and b[1] < max(bking[1],i) and b[0] == 0:
                        hit = False
                if hit == True:
                    hitcount+=2
                    print('RR')
            # This works with blocks


            # Check Other White Pieces in this Case Queens and Rooks
            # This only works if the pawn moves out of the way on row 1
            if bking[0] == 1:
                qr = whiteQ+whiteR
                for np in qr:
                    print(np)
                    if np[0] == 1:
                        ophit= True
                        for b in newblocks:
                            if b[1] > min(bking[1], np[1]) and b[1] < max(bking[1], np[1]) and b[0] == 1:
                                ophit = False
                        if ophit == True:
                            print('QR Hit')
                            hitcount+=4
            # New Disc hits works



            # Hits in the same col
            if bking[1] == i:
                for b in newblocks:
                    if b[0] > 0 and b[0] < bking[0] and b[1] == i:
                        hit = False
                if hit == True:
                    hitcount+=2
                    print("RC")
            # This Works With Blocks







            # For Diags work back from Black King's Location
            # If it hits the pawn then the pawn hits the bking
            # Absolute Difference will always be the same between coordinates
            if hit != False:
                diffx = abs(i - bking[1])
                diffy = abs(0 - bking[0])

                if diffx == diffy:
                    for b in newblocks:

                        diffblockx = abs(i - b[1])
                        diffblocky = abs(0 - b[0])

                        if diffblockx == diffblocky and diffblockx < diffx:
                            hit = False
                    if hit == True:
                        hitcount+=2
                        print('B',i)
            # This works with blocks
            if ophit == False:
                qb = whiteQ+whiteB
                #print(qb)
                for nqp in qb:
                    diffx = abs(nqp[1] - bking[1])
                    diffy = abs(nqp[0] - bking[0])
                    print(diffx,diffy)
                    ophit = True

                    if diffx == diffy:
                        for b in newblocks:

                            diffblockx = abs(i - b[1])
                            diffblocky = abs(0 - b[0])

                            if diffblockx == diffblocky and diffblockx < diffx:
                                ophit = False
                        if ophit == True:
                            hitcount+=4
                            print('QB',i)

    #print(board5)
    #print(bking)
    #print(hitcount)
    #print(blocks)
    #print(pawns)
    #print(whiteQ)
    return hitcount









board = ['########', '#k#P####', '########', '########', '########', '########', '#K######', '########']
board2 = ['########', '#P#P#P#P', '########', '####Q###', '###k####', '###r##p#', '#K######', '###R###K']


board = ['########', '##kP####', '########', '########', '########', '########', '#K######', '########']

board3 = ['########', '####P#P#', '####k###', '########', '########', '########', '#K######', '########']


# Block Test Cases
# Board 4 has 0 ways to check, one block
board4 = ['#####kQ#', '#######P', '########', '########', '########', '########', '########', '########']

# Board 5 has 0 ways to check, block on diag
board5 = ['########', '######QP', '#####k##', '########', '########', '########', '########', '########']

# Board 6 has 0 ways to check, block in col
board6 = ['########', '#######P', '#######Q', '#######k', '########', '########', '########', '########']



# Block Test Cases With Pawn Removal, the only way is on a diagonal

# Board 9 has 0 ways to check, block in col
board9 = ['########', '######PP', '#####k##', '########', '########', '########', '########', '########']


# Board 10 Random Assortment of Things
board10 = [['###Q####',
           '###P####',
           '########',
           '########',
           '########',
           '####k###',
           '########',
           '########']]



# Board 11 Discovered Checks, Row 1 Dis
board11 = [['########',
           '##QPk###',
           '########',
           '########',
           '########',
           '########',
           '########',
           '########']]

# Board 12 Discovered Checks, Diag
board12 = [['##Q#####',
            '###P####',
            '####k###',
            '########',
            '########',
            '########',
            '########',
            '########']]



# Multiple boards

boarda = [['########',
           '####kQPQ',
           '########',
           '########',
           '########',
           '########',
           '########',
           '########']]

boardb = [['########',
            '#k#P####',
            '########',
            '########',
            '########',
            '########',
            '########',
            '########']]



mass= []
mass.append(boarda)
mass.append(boardb)

for i in mass:
    print(waysToGiveACheck(i))

#result = waysToGiveACheck(board12)
#print(result)



"""
White
Q = Queen
R = Rook
B = Bishop
N = Knight
P = Pawn

Black
k = King




If it can be taken by a rook or bishop it can be taken by a queen.


Create all cases for QRBK, what cells they can get to
Then create blocks, pieces, theirs and ours that get in the way.


Steps:
accept input
find where our pawn(s) are and the black king is
create cases for QRBK based on all positions on row 8
create case where no pawns are on row 7, == 0
create block detection.





Knight Hits
Not affect by blocks
x,y coordinates
x range is 0 to 7
y can only be 1 or 2
left1d2 = [i-1,2]
left2d1 = [i-2,1]
right1d2 = [i+1,2]
righh2d1 = [i+2,1]




# Rook Hits
# Anything in row 0
# Anything up to row 7 in the same col






# Problems
Does moving my pawn remove that block and do my pawns block my own pieces?








"""





"""



Their Coding
# Note I changed the input from a list of lists, to a list of strings

#!/bin/python3

import sys

def waysToGiveACheck(board):
    # Complete this function

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        board = []
        for board_i in range(8):
           board_t = [str(board_temp) for board_temp in input().strip().split(' ')]
           board.append(board_t)
        result = waysToGiveACheck(board)
        print(result)

















"""































