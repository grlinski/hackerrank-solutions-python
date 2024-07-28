



# Filling Jars Mk2
# https://www.hackerrank.com/challenges/filling-jars/problem
# First was too slow,
# This time don't bother with Jars

def solve(n, operations):
    total = 0

    for i in operations:
        a = i[0]-1
        b = i[1]
        c = i[2]
        multi = b-a
        total = total+(multi*c)
    print(total//n)








ops = []

n,m = map(int,input().split(' '))
for i in range(m):
    x,y,z = map(int,input().split(' '))
    ops.append((x,y,z))

solve(n,ops)



















