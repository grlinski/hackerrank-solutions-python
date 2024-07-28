

# https://www.hackerrank.com/challenges/apple-and-orange/problem

"""


apple  = a, left
orange = b, right



d = distance fruit falls
postive = right
negative = left
this however is m for apples
and n for oranges



house = s to t

input
s t
a b
m n


"""


h1,h2 = map(int, input().split())
atree,otree = map(int, input().split())
m,n = map(int, input().split())
apples = list(map(int,input().strip().split(' ')))
oranges = list(map(int,input().strip().split(' ')))

acount = 0
for i in apples:
    j = i+atree
    if j >= h1 and j <= h2:
        acount+=1
ocount = 0
for i in oranges:
    j = i+otree
    if j >= h1 and j <= h2:
        ocount+=1



print(acount)
print(ocount)


























