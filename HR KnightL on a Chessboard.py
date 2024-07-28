

# KnightL on a Chessboard
# https://www.hackerrank.com/challenges/knightl-on-chessboard/problem

# Each Spot on the Grid is connected to others.Upwards of 8, minimum of 1
def createGrid(s,a,b):
    dict = {}

    for i in range(0,s):
        for j in range(0,s):
            x = (i,j)
            if i+a >0 and i+a <s and i+b >0 and i+b <s:
                x1 = (i + a, i + b)
                dict[x]+=x1
            if i + a > 0 and i + a < s and i - b > 0 and i - b < s:
                x2 = (i + a, i - b)
                dict[x] += x2
            if i - a > 0 and i - a < s and i + b > 0 and i + b < s:
                x3 = (i - a, i + b)
                dict[x] += x3
            if i - a > 0 and i - a < s and i - b > 0 and i - b < s:
                x4 = (i - a, i - b)
                dict[x] += x4
    grid = {}



createGrid(5,1,1)
#size = int(input())
















