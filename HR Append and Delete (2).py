#!/bin/python3

import math
import os
import random
import re
import sys
# HR Append  and Delete
# https://www.hackerrank.com/challenges/append-and-delete/problem



def amountOfSimilarity(a,b):

    counter = 0

    for i in range(0,len(a)):
        if a[i] == b[i]:
            counter+=1
        else:
            return counter


    return counter






# a is the smaller of a and b
def flowcontrol(a,b,k):
    diffLeng = abs(len(a)-len(b))
    simi = amountOfSimilarity(a,b)
    diffCharsA = len(a)-simi
    diffCharsB = len(b) -simi

    if simi == 0 and len(a)+len(b) <=k:
        return True
    if k-len(a) > len(b):
        return True


    a = a[:simi]
    k-=diffCharsA
    diffLeng = abs(len(a) - len(b))




    if k < 0:
        return False

    #print(a,b,k,diffLeng)
    # Only a few cases
    if diffLeng > k:
        #print('1')
        return False
    elif len(b) > len(a) and diffLeng <= k:
        if (diffLeng-k)%2 == 1:
            return False
        else:
            return True



        return True

    elif a==b and (k ==0 or k%2 ==0):
        return True
    elif a == b:
        if k >= len(a)*2:
            return True
    #print('pe')
    return False












# INPUTS
# Starter String
c = input()
# Desired String
d = input()
# Amount of Operations
k = int(input())


if len(c) <= len(d):
    a = c
    b = d
else:
    a = d
    b = c


ans = flowcontrol(a,b,k)
if ans == True:
    print('Yes')
else:
    print('No')

"""
Operations 
Add letters to the end of a string
Delete the last character in the string


"""
























