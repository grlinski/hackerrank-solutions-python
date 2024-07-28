

# Closest Numbers
# https://www.hackerrank.com/challenges/closest-numbers/problem

def quick_sort(seq):
    if len(seq) < 2 : return seq
    mid = len(seq)//2
    pi = seq[mid]
    seq = seq[:mid] + seq[mid+1:]
    lo = [x for x in seq if x <= pi]
    hi = [x for x in seq if x > pi]
    return quick_sort(lo) + [pi] + quick_sort(hi)


n = int(input())

q = list(map(int, input().strip().split(' ')))




q = quick_sort(q)


pairs = []
mini = 10000000
for i in range(0,len(q)-1):
    a = q[i]
    b = q[i+1]

    if abs(a-b) < mini:
        pairs = [a,b]
        mini = abs(a-b)
    elif abs(a-b) == mini:
        pairs.append(a)
        pairs.append(b)

for i in pairs:
    print(i,end=' ')






















