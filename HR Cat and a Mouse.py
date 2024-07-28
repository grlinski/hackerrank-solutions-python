
# Cat and a Mouse
# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

"""

Input
number of times
cat A location, cat b location mouse location



"""
#!/bin/python3

import sys

def catAndMouse(x, y, z):
    diffa = abs(x-z)
    diffb = abs(y-z)
    a = 'Cat A'
    b = 'Cat B'
    c = 'Mouse C'

    if diffa == diffb:
        return c
    elif diffa < diffb:
        return a
    else:
        return b



if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        x, y, z = input().strip().split(' ')
        x, y, z = [int(x), int(y), int(z)]
        result = catAndMouse(x, y, z)
        print (" ".join(map(str, result)))












