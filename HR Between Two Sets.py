
# https://www.hackerrank.com/challenges/between-two-sets/problem





"""

Two sets of integers A and B

All elements in A are factors of X
X is a factor of all elements in B


Input
# of elements in A, # elements in B
List of A
List of B


count how many numbers this could be

"""

n, m = map(int, input().split())
a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))


count = 0

for num in range(max(a), min(b)+1):
    bcorrect = 1
    acorrect = 1
    for anum in a:
        if num%anum != 0:
            acorrect = 0
    if acorrect ==1:
        for bnum in b:
            if bnum%num != 0:
                bcorrect = 0
    if bcorrect == 1 and acorrect == 1:
        count+=1




print(count)




"""
2 3
2 4
16 32 96


"""



