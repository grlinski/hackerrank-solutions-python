


# Athelete Sort
# https://www.hackerrank.com/challenges/python-sort-sort/problem



n,m = map(int, input().split(' '))

q = []
for i in range(n):
    s = list(map(int, input().strip().split(' ')))
    q.append(s)


k = int(input())
print(q)
print(k)


ans = sorted(q,key = lambda x: (x[k],x[0]))
for i in ans:
    for j in i:
        print(j,end=' ')
    print()