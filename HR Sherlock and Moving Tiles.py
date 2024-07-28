

# https://www.hackerrank.com/challenges/sherlock-and-moving-tiles/problem
# Sherlock and Moving Tiles

import math
def movingTiles(l, v1, v2, q):
    """
    :param l: Length of both Squares Sides
    :param v1: Velocity of Square 1
    :param v2: Veloctiy of Square 2
    :param q: List of size queries
    :print: Time when size of overlap of square1 and 2 is q
    """

    v = max(v2,v1)-min(v2,v1)
    v = math.sqrt((v**2)/2)
    # Find real velocity
    # Ie in the x or y direction.
    # Note both velocities are in the same direction, not different as I assumed


    for i in q:
        x = math.sqrt(i)
        t = (l-x)/v
        print(t)








l,s1,s2 = map(int, input().split(' '))
t = int(input())

q = []
for i in range(t):
    x = int(input())
    q.append(x)



print(movingTiles(l, s1, s2, q))














