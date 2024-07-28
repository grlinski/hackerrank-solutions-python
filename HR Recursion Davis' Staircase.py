

# Davis' Staricase
# https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=recursion-backtracking
"""
This is basically a sort of fibbonacci sequence
Except you add the previous 3 together to get the next item
Steps Amount
1 1
2 2
3 4
4 7
5 13
6 24
7 44
8 81


Solved
Note I left in now unsused code.
Previously I used stairCaseSolver and such to determine the pattern
And then way better implemented it.



"""




from itertools import permutations

def davisStaircase(steps):
    first = 1
    second = 2
    third = 4
    if steps == 1:
        return 1
    elif steps == 2:
        return 2
    elif steps == 3:
        return 4


    for i in range(3,steps):
        newNum = first+second+third
        first = second
        second = third
        third = newNum
    return third







def summer(x):
    total = 0
    for i in x:
        total+=i
    return total


def solveStairCases(steps):
    set1 = set()

    ones = [1]*steps
    twos = [2]*(steps//2)
    threes = [3]*(steps//3)

    allNum = ones+twos+threes
    perms = []
    for i in range(steps//3,steps):
        x = permutations(allNum,i)
        for j in x:
            if summer(j) == steps:
                set1.add(j)

    print(len(set1)+1)
    for i in set1:
        print(i)









staircases = int(input())
for i in range(staircases):
    steps = int(input())
    ans = (davisStaircase(steps))
    ans = ans%10000000007
    print(ans)

"""
Stepss, Amount

1 1
2 2
3 4
4 7
5 13
6 24
7 44
8 81



"""
