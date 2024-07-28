

# Big Sorting
# https://www.hackerrank.com/challenges/big-sorting/problem



def quick_sort(seq):
    if len(seq) < 2 : return seq
    mid = len(seq)//2
    pi = seq[mid]
    seq = seq[:mid] + seq[mid+1:]
    lo = [x for x in seq if x <= pi]
    hi = [x for x in seq if x > pi]
    return quick_sort(lo) + [pi] + quick_sort(hi)



n = int(input())
q = []
for i in range(n):
    x = int(input())
    q.append(x)



q = quick_sort(q)

for i in q:
    print(i)










