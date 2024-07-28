
# Time Complexity Primality
# https://www.hackerrank.com/challenges/ctci-big-o/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=miscellaneous


import math

def checkPrime(x):

    commonNumbers = [2,3,5,7,11]
    if x in commonNumbers:
        return True
    if x < 11:
        return False
    if (x-1)%6 == 0 or (x+1)%6 ==0:
        pass
    else:
        return False

    starter = 2
    upTo = int(math.sqrt(x))+1

    for i in range(starter,upTo):
        if x%i == 0:
            return False

    return True




n = int(input())
toCheck = []
for i in range(n):
    x = int(input())
    if checkPrime(x) == True:
        print('Prime')
    else:
        print('Not Prime')











