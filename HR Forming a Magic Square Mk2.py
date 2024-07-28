


# Forming a Magic Square
# https://www.hackerrank.com/challenges/magic-square-forming/problem

# This one works.

p0,p1,p2 = map(int, input().split(' '))
p3,p4,p5 = map(int, input().split(' '))
p6,p7,p8 = map(int, input().split(' '))

ms = [p0,p1,p2,p3,p4,p5,p6,p7,p8]


total = 0
x = [[2 ,7 ,6 ,9 ,5 ,1 ,4 ,3 ,8],
[2 ,9 ,4 ,7 ,5 ,3 ,6 ,1 ,8],
[4 ,3 ,8 ,9 ,5 ,1 ,2 ,7 ,6],
[4 ,9 ,2 ,3 ,5 ,7 ,8 ,1 ,6],
[6 ,1 ,8 ,7 ,5 ,3 ,2 ,9 ,4],
[6, 7, 2, 1, 5, 9, 8, 3, 4],
[8, 3, 4, 1, 5, 9, 6, 7, 2],
[8, 1, 6, 3, 5, 7, 4, 9, 2]]

mini= 1000000

for s in x:

    total = 0
    for i in range(0,9):
        total +=abs(ms[i]-s[i])
    mini = min(total,mini)



print(mini)













"""
Notes
Position 4 always needs to be 5, that is standard
Position 4 in this case is middle, middle.

Certain Numbers need to be in corners or middle of the sides.

Middles
9,1,3,7

Corners
4,2,8,6


Formations There are only 8 real formations. And They are basically all the same

Sides can be
4,9,2
2,9,4

4,3,8
8,3,4

8,1,6
6,1,8

2,7,6
6,7,2


Pairs
For the middles
9 will always be opposite 1
7 will always be opposite 3

Side Pairs
8 will be diagonal from 2
6 will be diagonal from 4


4 9 2
3 5 7
8 1 6











"""










































