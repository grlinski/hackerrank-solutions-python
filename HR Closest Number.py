
# Closest Number
# https://www.hackerrank.com/challenges/closest-number/problem

cases = int(input())

for i in range(cases):
    a,b,x = map(int, input().split(' '))
    ab = a**b

    # Two Cases First is When b is positive
    if b > -100000:
        rem = ab%x
        div = ab//x

        close1 = div*x
        close2 = close1+x
        # Then Check if the Multiple higher than ab is closer to ab.
        if abs(close2-ab) < abs(close1-ab):
            print(int(close2))
        else:
            print(int(close1))




















