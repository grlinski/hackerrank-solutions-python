


# ACM ICPC Team
# https://www.hackerrank.com/challenges/acm-icpc-team/problem


def countbits(x,dictc):
    s = str(x)
    count = 0
    for i in s:
        if i!='0':
            count+=1

    if count in dictc:
        dictc[count]+=1
    else:
        dictc[count] = 1

    return count,dictc





dictc = {}
t,u = map(int, input().split(' '))
q = []
for i in range(t):
    s = int(input())
    q.append(s)

ans = 0
maxi = 0
for i in range(0,len(q)-1):
    for j in range(i,len(q)):
        x = q[i]+q[j]
        newval,dictc = countbits(x,dictc)
        maxi = max(maxi,newval)

print(maxi)
print(dictc[maxi])






