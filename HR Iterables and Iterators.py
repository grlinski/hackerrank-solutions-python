

# Iterables and  Iterators
# https://www.hackerrank.com/challenges/iterables-and-iterators/problem

from itertools import combinations

n = int(input())
s = input().split()
k = int(input())


x = combinations(s, k)
numerator = 0
denominator = 0
for i in x:
    denominator+=1
    if 'a' in i:
        numerator+=1

print(numerator/denominator)



































