

# https://www.hackerrank.com/challenges/handshake/problem

# Handshake


"""

With n number of people, assuming every person shakes hands with everyother person once
How many handshakes are there?

First is number of cases
Then the number of people





2
1
2


"""


def numberofshakes(x):
    counter = 0
    for i in range(1,x):
        counter = counter+i
    print(counter)




T = int(input().strip())
for a0 in range(T):
    N = int(input().strip())
    numberofshakes(N)








"""
n = int(input())
list1 = []

for i in range(0,n):
    line = input()
    list1.append(line)

for i in list1:
    numberofshakes(i)




"""



















