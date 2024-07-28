

# HR Pythagorean Triple
# https://www.hackerrank.com/challenges/pythagorean-triple/problem

"""
One side must be even

a = u2-v2
b = uv
c = u2+v2

a = 2v+1
b = 2v2 +2v
c = 2v2+2v+1


Solve for v in either b or c formula




Where u and v are relatively prime intergers, not both odd




"""







import math





m = int(input())
n = int(input())

a = m**2 - n**2
b = 2*m*n
c = n**2+m**2

print(a)
print(b)
print(c)

# Removing m
a1 = 2*n+1
b1 = 2*n**2 +2*n
c1 = 2*n**2+2*n+1

print(a1)
print(b1)
print(c1)


# Change a1 and b1 into n
# A into n
# if a == 7, n == 3

n = (a1-1)/2

# b to n
# if b == 24 n == 3

(24)/2 = n**2 + n

12 = n*n+n
b/2 = n*n + n

x**2 + 1n