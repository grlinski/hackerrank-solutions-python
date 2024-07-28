

from itertools import count

# Beautiful Pairs
# https://www.hackerrank.com/challenges/beautiful-pairs/problem



n = int(input())


a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))


dicta = {}
dictb = {}
total=0

addsub = n

for i in range(n):
    x = a[i]
    y = b[i]

    # If the new number is present in the other dictionary
    # We can just subtract it from the other dictionary and add 1 to total
    if x in dictb and dictb[x] > 0:
        dictb[x]-=1
        total+=1
        addsub-=1
    elif x in dicta:
        dicta[x]+=1
    else:
        dicta[x]=1


    if y in dicta and dicta[y] > 0:
        dicta[y]-=1
        total+=1
        addsub-=1
    elif y in dictb:
        dictb[y]+=1
    else:
        dictb[y]=1


if addsub == 0:
    print(total-1)
else:
    print(total+1)








