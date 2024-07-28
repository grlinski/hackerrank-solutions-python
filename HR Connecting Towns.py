
# Connecting Towns
# https://www.hackerrank.com/challenges/connecting-towns/problem





cases = int(input())

for i in range(0, cases):
    towns = int(input())
    s = list(map(int, input().strip().split(' ')))
    total = 1
    for j in s:
        total = total * j
    print(total)












