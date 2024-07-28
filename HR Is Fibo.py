
# Is Fibo
# https://www.hackerrank.com/challenges/is-fibo/problem
import math

def isfibo(x):
    y =((x**2)*5)-4
    z = ((x**2)*5)+4

    minus = issquare(y)
    plus = issquare(z)

    if minus or plus:
        return 'IsFibo'
    else:
        return 'IsNotFibo'



def issquare(x):
    z = int(math.sqrt(x))
    y = z**2
    if y == x:
        return True
    else:
        return False





times = int(input())

for i in range(times):
    x = int(input())
    print(isfibo(x))















