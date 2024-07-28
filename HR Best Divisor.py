



# Best Divisor
# https://www.hackerrank.com/challenges/best-divisor/problem

def summer(x):
    y = str(x)
    total = 0
    for i in y:
        z = int(i)
        total = total+z
    return total


x = int(input())

top = x//2
divs = []
for i in range(1,top+1):
    if x%i == 0:
        divs.append(i)
divs.append(x)

q = []
for i in divs:
    j = summer(i)
    q.append(j)

#print(q)
#print(divs)

bestdiv = 10000000

# Want Highest Sum First
bestsum = 0

for i in range(0,len(q)):

    #print(q[i],bestsum)
    if q[i] > bestsum:
        bestsum = q[i]
        bestdiv = divs[i]
    elif q[i] == bestsum:
        if divs[i] < bestdiv:
            bestsum = q[i]
            bestdiv = divs[i]



print(bestdiv)






