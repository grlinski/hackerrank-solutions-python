

# Array Manipulation
# https://www.hackerrank.com/challenges/crush/problem

n,ops = map(int, input().split(' '))

q = [0]*n



for i in range(ops):
    a,b,k = map(int, input().split(' '))

    for j in range(a-1,b):
        q[j] = q[j]+k


print(max(q))



















