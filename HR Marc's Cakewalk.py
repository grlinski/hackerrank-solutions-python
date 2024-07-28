

# Marc's Cakewalk
# https://www.hackerrank.com/challenges/marcs-cakewalk/problem


n = int(input())
c = list(map(int, input().strip().split(' ')))


d = sorted(c)
e = d[::-1]

total = 0

for i in range(0,len(e)):
    total += (2**i*(e[i]))

print(total)









