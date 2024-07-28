
# https://www.hackerrank.com/challenges/random-number-generator/problem
# Random Number Generator


"""

The problem is fairly easy if you restate the question as follows:
 You have a rectangle with corners: (0,0) (a,0) (0,b), (a,b),
  and a triangle with vertices (0,0) (0,c) (c,0).
  What fraction of the rectangle is covered by the triangle?


Okay so
We generate two numbers
From 0 to a
and  0 to b
What is the chance that randomly generated and added, they are greater than c?





"""

import random
from fractions import Fraction
maxa = 1
maxb = 1
maxc = 2

#a = random.randint(0,maxa+1)
#b = random.randint(0,maxb+1)
#c = random.randint(0,maxc+1)


a = 2
b = 8
c = 10

#print(a,b,c)
more = 0
less = 0
total = 0
for i in range(0,a+1):
    for j in range(0,b+1):
        if i+j < c:
            less+=1
            total+=1
        elif i+j > c:
            total+=1


if less/total == 1:
    print('1/1')
else:
    print(Fraction(less/total))




















