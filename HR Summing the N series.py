

# Summing the N Series

# https://www.hackerrank.com/challenges/summing-the-n-series/problem

# Very easy


def summingSeries(n):

    total = 0
    for i in range(1,n+1):
        temp =  (i**2)-((i-1)**2)

        total = total + temp

        print(i,temp,total)

    return total%((10**9)+7)

# Both work but below is the easy version, once I figured out the sequence
"""
def summingSeries(n):

    total = n**2

    return total%((10**9)+7)
"""
x = int(input())
print(summingSeries(x))












