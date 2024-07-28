

# Ways to Give a Check
# https://www.hackerrank.com/contests/w36/challenges/ways-to-give-a-check

# Stripped Down Version

def waysToGiveACheck(board):

    # Setup
    # Items are stored as row,col
    pawns = []
    blocks = []
    bking = []
    hitcount = 0

    # Sort out Where Everything is
    # Pawns, King, Blocks
    # Note most everything is stored as row,col
    # Except pawns which are just col since the row is always 0
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

    # Determine How Many Checks for a Certain Pawn Promotion
    for i in pawns:
        # Knight Moves, if the Knight Hits Nothing Else Does
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


        # New Block List
        # This contains the blocks without the current pawn
        # Blocks will not affect Knights
        newblocks = blocks
        currentpawn = [1,i]
        newblocks.remove(currentpawn)


        # Rook Moves
        # Horizontal on Row 0
        hit = True
        if bking [0] == 0:
            for b in newblocks:
                if b[1] > min(bking[1],i) and b[1] < max(bking[1],i) and b[0] == 0:
                    hit = False
            if hit == True:
                hitcount+=2

        # Rook Moves on the column
        elif bking[1] == i:
            for b in newblocks:
                if b[0] > 0 and b[0] < bking[0] and b[1] == i:
                    hit = False
            if hit == True:
                hitcount+=2


        # Bishops Moves
        # Diagonals, if the abs difference is equal on row and col, the pawn will hit the king assuming no block
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

    return hitcount






# Board 10 Random Assortment of Things
board10 = ['########', '####P###', '########', '########', '########', '####k###', '########', '########']



result = waysToGiveACheck(board10)
print('asda')
print(result)















