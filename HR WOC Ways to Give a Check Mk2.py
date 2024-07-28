# Note AFAICT This Version Works Perfectly
# It has pretty damned great comments, however it is very cluttered
# So I'm going to create a third version that is stripped down

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

    # For My Pawns All I care about is row1, so I only have it's col position
    pawns = []
    # Everything but my pawns and the black king are blocks
    # This is stored as a lists within lists, x y coordinates
    # At most two blocks, only 4 pieces on the board, min 1 pawn, 1 bking, 1 white king, possibly 1 other piece
    blocks = []
    location = []
    # The Singular Black King stored as two values, x and y
    bking = []
    row1 = board[1]


    # Hits Where the Promoted Pieces Can Get to
    hits = []
    hitcount = 0

    # Where Is Everything?
    # Pawns, King, Blocks
    # Note most everything is stored as row,col
    # Except pawns which are just col
    for i in range(0,8):
        for j in range(0,8):
            if board[i][j] == 'P':
                pawns.append(j)
                location = []
                location.append(i)
                location.append(j)
                blocks.append(location)
            elif board[i][j] == 'k':
                bking.append(i)
                bking.append(j)
            elif board[i][j] != '#':
                location = []
                location.append(i)
                location.append(j)
                blocks.append(location)
    # Works Up to Here
    # Stored all positions


    # Case 1, no Pawns on Row 1, Therefore no ways to check
    # Nevermind, always at least one pawn



    #Knight Hits, Not Affected By Blocks
    # Later Only count hits, no need to do more
    # Store Values in list, since we need to count each individual hit
    # A knight can only hit the king once so if we get a hit there's no point in continuing
    # Also no need to store the values for later, just keep hitcount
    for i in pawns:

        # Knight Moves, if the Knight Hits Nothing Else Does
        # Checks if the Knight hits the King
        # Range for x 0 to 7,
        # Don't Worry About Blocks for Knight Moves
        q = [i - 1, 2]
        left1d2 = [i - 1, 2]
        left2d1 = [i - 2, 1]
        right1d2 = [i + 1, 2]
        righh2d1 = [i + 2, 1]

        if left1d2 == bking:
            hitcount+=1
        elif left2d1 == bking:
            hitcount+=1
        elif right1d2 == bking:
            hitcount+=1
        elif righh2d1 == bking:
            hitcount+=1

        # Knight Hits Works AFAICT



        # New Block List
        # First Step is to Create a New List of Blocks without the Current Pawn
        # The Current Pawn is always in row 1
        # Note I realized I have been storing info as row, col not x,y
        # I'm going ot continue with row,col and hopefully it all works out
        newblocks = blocks
        currentpawn = [1,i]
        newblocks.remove(currentpawn)


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
        hit = True
        if bking [0] == 0:
            for b in newblocks:
                if b[1] > min(bking[1],i) and b[1] < max(bking[1],i) and b[0] == 0:
                    hit = False
            if hit == True:
                hitcount+=2
        # Hits in the same col
        elif bking[1] == i:
            for b in newblocks:
                if b[0] > 0 and b[0] < bking[0] and b[1] == i:
                    hit = False
            if hit == True:
                hitcount+=2

        # For Diags work back from Black King's Location
        # If it hits the pawn then the pawn hits the bking
        # Absolute Difference will always be the same between coordinates
        else:
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


    #print(bking)
    #print(hits)
    #print(hitcount)
    #print(blocks)
    return hitcount









board = ['########', '#k#P####', '########', '########', '########', '########', '#K######', '########']
board2 = ['########', '#P#P#P#P', '########', '####Q###', '###k####', '###r##p#', '#K######', '###R###K']


board = ['########', '##kP####', '########', '########', '########', '########', '#K######', '########']

board3 = ['########', '####P#P#', '####k###', '########', '########', '########', '#K######', '########']



result = waysToGiveACheck(board3)
print(result)



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































