

# Leonardo's Prime Factors
# https://www.hackerrank.com/challenges/leonardo-and-prime/problem

n = int(input())

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
          43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
          101, 103, 107, 109, 113, 127, 131, 137, 139, 149,
          151, 157, 163, 167, 173, 179, 181, 191, 193, 197,
          199, 211, 223, 227, 229]


def primeCount(n):
    pos = 0
    total = 1
    count = 0

    if n == 0 or n== 1:
        return 0

    while True:
        total = total*primes[pos]

        if total > n:
            return count
        elif total <= n:
            pos+=1
            count +=1

















