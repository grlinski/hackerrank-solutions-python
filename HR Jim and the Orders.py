


# Jim and the Orders
# https://www.hackerrank.com/challenges/jim-and-the-orders/problem





n = int(input())


s = []
dict = {}

for i in range(n):
    o,p = map(int, input().split(' '))
    x = o+p

    y = str(x)

    if y in dict:
        dict[y]+=(' '+str(i+1))
    else:
        dict[y]=str(i+1)


    s.append(x)

s=sorted(set(s))
#print(dict)
#print(s)

for i in s:
    j = str(i)
    print(dict[j],end=' ')





