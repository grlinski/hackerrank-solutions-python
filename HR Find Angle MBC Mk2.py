


# Find Angle MBC
# https://www.hackerrank.com/challenges/find-angle/problem

import math


AB = 10
BC = 10
b = 90

# Hyp
HYP = math.sqrt(AB**2 + BC**2)
c = math.degrees(math.asin(AB/HYP))
a = math.degrees(math.asin(BC/HYP))

print(round(c),end='°')

# Creating a new Triangle
"""
M B C
BC is the same
c is the same
The new b is less than 90
MC is half of HYP

AM=BM=CM

"""














































