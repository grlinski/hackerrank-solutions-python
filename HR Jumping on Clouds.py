#!/bin/python3

import math
import os
import random
import re
import sys




n = int(input())
clouds = input().split()

#print(clouds)

"""
Avoid 1
Staring at pos0 get to -1
Can jump in 1's or 2's


"""

total = 0
i=0
while True:
    if i ==len(clouds)-1:
        break
    if i ==len(clouds)-2:
        total+=1
        break
    if i ==len(clouds)-3:
        total+=1
        break



    cur = clouds[i]
    c2 = clouds[i+1]
    c3 = clouds[i+2]



    if c3 == '0':
        i+=2
        total+=1
    else:
        i+=1
        total+=1


print(total)

























