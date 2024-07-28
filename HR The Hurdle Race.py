

# Hurdle Race
# https://www.hackerrank.com/challenges/the-hurdle-race/problem



"""


input
number of hurdles, jump height
hurdle heights



"""
n,k = map(int, input().split(' '))
height = list(map(int, input().strip().split(' ')))

height.sort()
x = height[-1]-k
if x < 0:
    return 0
else:
    return x

















