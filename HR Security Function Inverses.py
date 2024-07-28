


# Security Function Inverses
# https://www.hackerrank.com/challenges/security-inverse-of-a-function/problem


n = int(input())
s = list(map(int, input().strip().split(' ')))
dict = {}
for i in range(1,n+1):
    dict[s[i-1]] = i

#print(dict)
for i in range(1,n+1):
    print(dict[i])











