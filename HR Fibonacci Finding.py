
# Fibonacci Finding
# https://www.hackerrank.com/challenges/fibonacci-finding-easy/problem


def fib(n):
    F = [[1, 1],
         [1, 0]]
    if (n == 0):
        return 0
    power(F, n - 1)

    return F[0][0]


#tc = int(input())
tc = 1


for i in range(tc):
    a, b, n = map(int, input().split(' '))
    ans = fib(n)
    print(ans)


























