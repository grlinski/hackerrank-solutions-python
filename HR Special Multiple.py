

# Special Multiple

# https://www.hackerrank.com/challenges/special-multiple/problem

def solve(n):
    s =  str(n)
    """

    """

    count = 1
    while True:
        biny = bin(count)
        r = str(biny[2:])
        s = ''
        for i in r:
            if i == '1':
                s +='9'
            else:
                s+='0'

        x = int(s)

        if x%n == 0:
            return x

        count+=1






n = int(input())

print(solve(n))



















