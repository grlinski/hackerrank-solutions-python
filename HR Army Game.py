

# Army Game
# https://www.hackerrank.com/challenges/game-with-cells/problem


"""

n = rows
m = columns


def supply(rows,cols):
    size = rows*cols



"""


def supply(rows,cols):
    total = 0
    # Squares
    total = total+((rows//2)*(cols//2))
    # Leftovers
    if rows%2!=0:
        total = total+cols//2
    if cols%2!=0:
        total = total+rows//2
    if cols%2!= 0 and rows%2!=0:
        total = total+1
    return total




n = 5
m = 3

print(supply(n,m))




