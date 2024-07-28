


#!/bin/python3

import sys



# Note I made some changes to their way of doing this problem
# First I didn't store the board as a list of lists, because it wasn't really needed
# Second the top row to me is row 0, in their version it is row 8
# Again this just makes things easier for me and doesn't change anything




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
    for i in range(0,8):
        for j in range(0,8):
            if board[i][j] == 'P':
                pawns.append(j)
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
        # Range for x 0 to 7,
        x = i-1
        if x >-1:
            q = [i-1,2]
            if q == bking:
                hitcount+=1
                break
            hits.append([i-1,2])
        x = i-2
        if x >-1:
            q = [i-2,1]
            if q == bking:
                hitcount+=1
                break
            hits.append([i-2,1])
        x = i +1
        if x < 8:
            q = [i + 1, 2]
            if q == bking:
                hitcount+=1
                break
            hits.append([i + 2, 2])
        x = i +2
        if x < 8:
            q = [i + 2, 1]
            if q == bking:
                hitcount+=1
                break
            hits.append([i + 2, 1])
    # Knight Hits Works AFAICT
    print(hits)

    # Rook Hits, Add Queen and Bishop Later
    # If the Rook Hits the Queen Hits Too, same idea with the Bishop
    # Later add in blocks

    for i in pawns:
        # I only care about the king in row zero or the same col
        # This is for queens and rooks thus +2
        if bking [0] == 0:
            hitcount+=2
        # Hits in the same col
        elif bking[1] == i:
            hitcount+=2
        # For Diags work back from Black King's Location
        # If it hits the pawn then the pawn hits the bking
        # Absolute Difference will always be the same between coordinates
        else:
            diffx = abs(i - bking[0])
            diffy = abs(0 - bking[1])
            if diffx == diffy:
                hitcount+=2

    #print(bking)
    #print(hits)
    #print(hitcount)
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






























