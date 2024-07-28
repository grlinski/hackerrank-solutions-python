


# Reverse Game
# https://www.hackerrank.com/challenges/reverse-game/problem


def rev_ball(n,k):
    midpoint = (n-1) / 2
    n = n-1

    if k == midpoint:
        return n
    elif k < midpoint:
        return (k*2)+1
    elif k > midpoint:
        return(n-k)*2






n,k = map(int,input().split(' '))

print(rev_ball(n,k))








