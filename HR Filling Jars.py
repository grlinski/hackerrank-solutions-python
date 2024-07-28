
# Filling Jars
# https://www.hackerrank.com/challenges/filling-jars/problem


def solve(n, operations):
    jars = [0]*n

    for i in operations:
        a = i[0]-1
        b = i[1]
        c = i[2]
        for j in range(a,b):
            jars[j]+=c
    print(sum(jars)//n)








ops = []

n,m = map(int,input().split(' '))
for i in range(m):
    x,y,z = map(int,input().split(' '))
    ops.append((x,y,z))

solve(n,ops)










