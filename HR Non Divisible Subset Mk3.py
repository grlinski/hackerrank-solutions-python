


# Non-Divisble Subset
# https://www.hackerrank.com/challenges/non-divisible-subset/problem
"""
Misread nothing in the subset can pair to be divisible by k


New idea divide everything by k
Sort by remainders
If k == 5 and remainders are 1 and 4, those numbers cannot be together.

Getting Closer I think

Main problem is likely special cases

Problems like where the original remainder is zero.

And another where div/k is even and remainder is half of that.


Getting closer, latest iteration is the closest.
Maybe check an unworking problem.


"""




n,div = map(int, input().split(' '))
numbers = list(map(int, input().strip().split(' ')))

pairs = {}
subsets = []
for i in numbers:
    subsets.append([i])

#print(subsets)

dict = {}

for i in range(0,len(numbers)):
    x = numbers[i]
    rem = (x%div)
    if rem in dict:
        dict[rem] += 1
    else:
        dict[rem] = 1

maxi = 0
subsets = []

listofrem = []
for i in dict:
    listofrem.append(i)
for i in listofrem:
    x = [i]
    subsets.append(x)


#print('here')
#print(subsets)
#print(listofrem)

for i in range(0,len(listofrem)):
    x = listofrem[i]

    for j in range(0, len(subsets)):

        toAdd = True
        for k in range(0, len(subsets[j])):
            y = subsets[j][k]
            if x == y:
                pass
            elif (x + y) % div == 0:
                toAdd = False
                break
        if toAdd == True:
            if len(subsets) == 1 and subsets[0] == x:
                pass
            else:
                subsets[j].append(x)


maxi = 0
if 0 in dict:
    dict[0] = 1

if div%2==0:
    half = div//2
    if half in dict:
        dict[half] = 1


for i in subsets:
    total = 0
    si = set(i)
    si = list(si)
    for j in si:
        total += (dict[j])
    print(total)
    maxi = max(maxi,total)

print(maxi)

for i in subsets:
    print(i)
print('REM')
total = 0
for i in listofrem:
    total+=dict[i]


print(total)






