
# Minimum Distances
# https://www.hackerrank.com/challenges/minimum-distances/problem



n = int(input())

a = list(map(int, input().rstrip().split()))


dict = {}
mini = 10000000
for i in range(0,len(a)):
    b = a[i]
    if b in dict:
        c = dict[b]
        d = abs(c-i)
        mini = min(d,mini)
        dict[b] = i
    else:
        dict[b] = i

if mini == 10000000:
    print(-1)
else:
    print(mini)














