


# The Coin Change Problem
# https://www.hackerrank.com/challenges/coin-change/problem



n,c = map(int, input().split(' '))

q = list(map(int, input().strip().split(' ')))

ways = 0
coins = []
for i in q:
    if i < n:
        coins.append(i)
    elif i== n:
        ways+=1

coins.sort()
print(coins)





























