
# Chocolate Feast
# https://www.hackerrank.com/challenges/chocolate-feast/problem


"""
n = inital money
c = cost of candy
m = wrapper returns for 1 free chocolate


"""




t = int(input())





for i in range(t):

    n, c, m = map(int, input().split(' '))
    ans = 0

    w = n//c
    ans+=w
    n = n%c


    while w > m-1:
        nw = w//m
        ans+=nw


        w = w%m + (nw)


    print(ans)










