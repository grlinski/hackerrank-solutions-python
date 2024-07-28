

# Sherlock and Permutations
# https://www.hackerrank.com/challenges/sherlock-and-permutations/problem

import itertools

def solve(n, m):
    list1 = [0]*n
    list2 = [1]*m
    list3 = list1+list2

    x = (list(itertools.permutations(list3, len(list3))))
    total = set(x)
    ans = 0

    for i in total:
        if i[0] == 1:
            ans += 1
    return ans/(10**9+7)




t = int(input())

for i in range(t):
    n,m = map(int,input().split())

















