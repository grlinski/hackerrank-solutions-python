import time
#Migratory Birds HackerRank
#https://www.hackerrank.com/challenges/migratory-birds?h_r=next-challenge&h_v=zen

# Basically what is the most common number?

start = time.time()

n = int(input())
ar = list(map(int, input().strip().split(' ')))
ar2 = []

for i in range(0,n):
    ar2.append(0)

for i in ar:
    ar2[i] = ar2[i]+1

topmost = 0
newval = 0
result = 0

for i in range(0,n):
    newval = ar2[i]
    if newval > topmost:
        topmost = newval
        result = i


print(result)
end = time.time()
print(end-start)






"""
Sample Data

6
1 4 4 4 5 3

"""








