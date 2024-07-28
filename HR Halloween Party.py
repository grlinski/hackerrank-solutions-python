

# Halloween Party
# https://www.hackerrank.com/challenges/halloween-party/problem


def halloweenParty(k):
    # If even
    if k%2 == 0:
        y = k//2
        return y*y
    else:
        y = k//2
        x = y+1
        return x*y




t = int(input())
for i in range(t):
    x = int(input())
    halloweenParty(x)










