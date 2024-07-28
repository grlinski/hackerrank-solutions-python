

# Connecting towns

# https://www.hackerrank.com/challenges/connecting-towns/problem

def connectingTowns(n, routes):
    total = 1

    if len(routes) == 1:
        return routes[0]
    for i in routes:
        total = total*i

    return total%1234567




t = int(input())


s = list(map(int, input().strip().split(' ')))



print(connectingTowns(0,s))





