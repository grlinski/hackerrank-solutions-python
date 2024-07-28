
# https://www.hackerrank.com/challenges/the-birthday-bar/problem






"""

row of n sqaures
each square has an integer on it
Ron's birthday falls on month m and day d

Given m and d and a sequence of integers written on each square
How many ways can we break chocolate pieces to satisfy this requirement

input
number of choco pieces
integer list on consequetive pieces
day and month of Ron's birthday d and m

so ints must add up to d
pieces must add up to m


"""


n = map(int, input())
s = list(map(int, input().strip().split(' ')))
d,m = map(int, input().split(' '))

count = 0
for start in range(0,len(s)):
    dcorrect = False
    mcorrect = False
    total = 0
    pieces = 0
    for i in range(start,len(s)):
        pieces = pieces+1
        total = total+s[i]
        if pieces == m and total == d:
            count+=1


print(count)








"""
5
1 2 1 3 2 
3 2



"""













