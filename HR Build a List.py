
# Building a List
# https://www.hackerrank.com/challenges/building-a-list/problem

import itertools

def sub_strings(x):
    ml = []
    for i in range(1,len(x)+1):
        q = (list(itertools.combinations(x, i)))
        for j in q:
            ml.append(j)

    list_to_string(ml)

def list_to_string(x):

    q = []
    for i in range(0,len(x)):
        y = ''
        y = y.join((x[i]))
        q.append(y)
    q.sort()
    for i in q:
        print(i)







times = int(input())

for i in range(times):
    leng = int(input())
    q = []
    x = input()
    for i in x:
        q.append(i)

    sub_strings(q)
























