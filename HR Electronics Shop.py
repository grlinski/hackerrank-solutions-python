
# Electronics Shop
# https://www.hackerrank.com/challenges/electronics-shop/problem


"""





input
money, number of keyboard brands, number of USB brands
prices of the keyboard brands
prices of the USB brands

s,n,m
ni
mi


"""



def getMoneySpent(keyboards,drives,s):
    current = 0
    total = 0
    canbuy = False
    for i in keyboards:
        for j in drives:

            total = i + j
            if total <= s:
                canbuy = True
                current = max(total,current)

    if canbuy:
        return current
    else:
        return -1








s,n,m = map(int, input().split(' '))

keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))



moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)















