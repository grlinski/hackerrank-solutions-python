



import math

n = int(input())


q = list(map(int, input().strip().split(' ')))

x = sorted(q)
ans = -1
for i in range(len(x)-1,1,-1):
    a = x[i]
    b = x[i-1]
    c = x[i-2]

    #print(a,b,c)

    if a==b==c or a==b:
        ans=(c,b,a)
        break
    elif a>= b+c:
        pass

    else:
        ans = (c,b,a)

if ans == -1:
    print(ans)
else:
    for i in ans:
        print(i,end=' ')














