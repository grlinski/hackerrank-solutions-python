

from collections import defaultdict



d = defaultdict(list)

set1 = set()



t,items = map(int, input().split(' '))

for i in range(t):
    x = input()
    d[x].append(i+1)
    set1.add(x)

#print(set1)
for i in d:
    x = (" ".join(map(str, d[i])))
    #print(i)
    if i in set1:
        print(x)
    else:
        print(-1)













