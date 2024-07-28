


"""
NTS
This was an awfully worded problem, I had to go through it a few times to understand.
Eventually once I got it mostly working I ran into a few problems.
One of the most annoying ones was that one of the testcases I downloaded didn't load entirely.
So I only had a portion of the test and it didn't fully run.
So nexttime check that
Second I forgot to print properly for the -1 section.
I ended up with too many spaces.
So remember to check printing too.


"""


# DefaultDict Tutorial
# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
#
from collections import defaultdict

d = defaultdict(list)

#d['python'].append("awesome")
#d['something-else'].append("not relevant")
#d['python'].append("language")

n,m = map(int, input().split(' '))


for i in range(n):
    x = input()
    d[x].append(i+1)


words = []

for i in range(m):
    words.append(input())

for i in words:
    if i in d:
        x = d[i]
        for j in x:
            print(j,end=' ')
    else:
        print('-1',end='')
    print()




























