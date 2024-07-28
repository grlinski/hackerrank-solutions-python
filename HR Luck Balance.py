


# Luck Balance
# https://www.hackerrank.com/challenges/luck-balance/problem

n,k = map(int, input().split(' '))

luck = 0

imp = []
uni = []

for i in range(n):
    L,T= map(int, input().split(' '))

    if T == 1:
        imp.append(L)
    else:
        luck+=L

imp=sorted(imp)

for i in range(len(imp)-1,-1,-1):
    if k==0:
        luck-=imp[i]
    else:
        luck+=imp[i]
        k-=1



print(luck)









