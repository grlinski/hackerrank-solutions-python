
# Missing Numbers
# https://www.hackerrank.com/challenges/missing-numbers/problem



dict={}
pntls = input()
a = list(map(int, input().split()))

pntls = input()
b = list(map(int, input().split()))

countA = [0]*10001
countB = [0]*10001

for i in a:
    countA[i]+=1
for i in b:
    countB[i]+=1

for i in range(0,len(countA)):
    if countA[i]!=countB[i]:
        print(i,end=' ')












