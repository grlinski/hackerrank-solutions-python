
# https://www.hackerrank.com/challenges/magic-square-forming/problem

# Forming a Magic Square Mk??


p0,p1,p2 = map(int, input().split(' '))
p3,p4,p5 = map(int, input().split(' '))
p6,p7,p8 = map(int, input().split(' '))

ms = [p0,p1,p2,p3,p4,p5,p6,p7,p8]

# Total cost of changing
total = 0
if p4 != 5:
    total += abs(p4-5)























