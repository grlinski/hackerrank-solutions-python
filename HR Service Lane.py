
# Service Lane
# https://www.hackerrank.com/challenges/service-lane/problem
# Mostly done on the Hackerrank Page, done



def serviceLane(n, a, b, w):
    ans = min(w[a:b + 1])
    return ans


n,t = map(int, input().split(' '))

w = list(map(int, input().strip().split(' ')))


for _ in range(t):
    a,b = map(int, input().split(' '))







