

# Pairs
# https://www.hackerrank.com/challenges/pairs/problem

n,k = map(int, input().split(' '))
list1 = list(map(int, input().strip().split(' ')))
setA = set(list1)
setB = set()
for i in list1:
    x = i+k
    setB.add(x)

c = (setA & setB)

print(len(c))













