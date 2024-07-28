

# Constructing a Number
# https://www.hackerrank.com/challenges/constructing-a-number/problem

"""
If the digits sum to 3 6 or 9 it is divisible by 3


"""




def sum_digits(x):
    total = 0
    for i in x:
        for j in i:
            total = total+int(j)

    stotal = str(total)
    if stotal != 1:
        total = 0
    else:
        return total

    while len(stotal) != 1:
        for i in stotal:
            total = total+int(i)
        stotal = str(total)

    total = int(stotal)
    return total





cases = int(input())

for i in range(0,cases):
    items = int(input())
    q = input().split()
    ans = (sum_digits(q))
    if ans == 3 or ans == 6 or ans ==9:
        print('Yes')
    else:
        print('No')









