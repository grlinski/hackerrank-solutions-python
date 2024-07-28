
# Extra Long Factorials
# https://www.hackerrank.com/challenges/extra-long-factorials/problem



def extraLongFactorials(n):
    total = 1
    for i in range(n,0,-1):
        total = total*i
    return total


q = 25
print(extraLongFactorials(q))














