



# K Candy Store
# https://www.hackerrank.com/challenges/k-candy-store/problem
import itertools

#def solve(candies, money):
def combinations(n, k):



    top = 1
    b1 = 1
    b2 = 1
    for i in range(1, n + 1):
        top = top * i
    for i in range(1, k + 1):
        b1 = b1 * i
    for i in range(1, n - k + 1):
        b2 = b2 * i
    answer = int(top / (b1 * b2))
    return answer





t = int(input())


for i in range(t):
    n = int(input())
    k = int(input())
    print(combinations(n,k))

























