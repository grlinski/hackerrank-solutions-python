


# Hallowen Sale
# https://www.hackerrank.com/challenges/halloween-sale/problem


"""
first game sold at p
subsequent games sold for d less than pervious
until price hits m, then games are sold at m
s is how much money you start with.

How many games can you buy


"""

p,d,m,s = map(int, input().split(' '))


ans = 0

if p > s:
    ans = 0
else:
    s=s-p
    if p-d < m:
        d = 0
        p = m

    else:

        p=p-d
    ans+=1

    while s>-1:


        #print(s,p,ans)

        if s-p > -1:
            ans+=1
            s -=p
        else:
            break

        if p -d > m:
            p-=d
        else:
            d = 0
            p=m



print(ans)










