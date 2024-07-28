


# Cavity Map
# https://www.hackerrank.com/challenges/cavity-map/problem


n = int(input())

a = []
ans = []

for i in range(n):
    s = input()
    b = []
    for j in s:
        b.append(j)
    a.append(b)
    ans.append(b)


print(a)

for i in range(1,n-1):
    for j in range(1,n-1):
        c = a[i][j]
        u = a[i-1][j]
        d = a[i+1][j]
        r = a[i][j+1]
        l = a[i][j-1]

        if c > u and c > d and c > r and c > l:

            ans[i][j] = 'X'

for i in ans:
    for j in i:
        print(j,end="")
    print()











