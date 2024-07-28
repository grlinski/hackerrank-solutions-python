

# Friend Circle Queries
# https://www.hackerrank.com/challenges/friend-circle-queries/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=miscellaneous

"""
Seems to work
However timed out on half of the cases




"""




times = int(input())
maxi = 2
allSets = []

for t in range(times):
    a,b = map(int, input().split(' '))

    already = False
    newSet = set()
    newList = []
    for i in range(0,len(allSets)):
        maxi = max(maxi,len(allSets[i]))
        if a in allSets[i] or b in allSets[i]:
            allSets[i].add(a)
            allSets[i].add(b)
            for j in allSets[i]:
                newSet.add(j)
            allSets[i] = newSet
            already = True
        else:
            newList.append(allSets[i])
        newList.append(newSet)
        maxi = max(maxi, len(newSet))
    if already == False:
        newList.append({a,b})
    allSets = []
    for i in newList:
        allSets.append(i)

    print(maxi)






















