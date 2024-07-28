

# Jumping on the Clouds R
# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem
import random


def jumpingOnClouds(c, k):
    numc = len(c)
    E = 100
    pos = 0

    for i in range(0,n,k):
        x = c[i]
        if x == 0:
            E = E-1
        else:
            E = E-3




    return E





# Data Gen
"""
2<= n <= 25
1 <= k <= n
n%k == 0
c either 1 or 0


"""
n = 1
k = 2

while n%k !=0:
    n = random.randint(2,25)
    k = random.randint(1,n)
c = []
for i in range(0,n):
    x = random.randint(0,1)
    c.append(x)

#jump = 2
#clouds = [0,0,1,0,0,1,1,0]
print(n,k)
print(c)

print(jumpingOnClouds(c,k))












