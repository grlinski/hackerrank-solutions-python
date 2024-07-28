

# Non-Divisble Subset
# https://www.hackerrank.com/challenges/non-divisible-subset/problem
"""
Misread nothing in the subset can pair to be divisible by k


"""



from itertools import count



n,div = map(int, input().split(' '))
numbers = list(map(int, input().strip().split(' ')))

pairs = {}
subsets = []
for i in numbers:
    subsets.append([i])

#print(subsets)



for i in range(0,len(numbers)):
    x = numbers[i]
    for j in range(0,len(subsets)):


        toAdd = True
        for k in range(0,len(subsets[j])):
            y = subsets[j][k]
            if x == y:
                pass
            elif (x+y)%div ==0:
                toAdd = False
                break
        if toAdd == True:
            if len(subsets)==1 and subsets[0] == x:
                pass
            else:
                subsets[j].append(x)

maxi = 0
for i in subsets:
    length = len(set(i))
    maxi = max(maxi,length)
print(maxi)

for i in subsets:
    print(i)














