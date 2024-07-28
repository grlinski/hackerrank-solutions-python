

n,k = map(int, input().split(' '))
s = list(map(int, input().strip().split(' ')))



def quick_sort(seq):
    if len(seq) < 2 : return seq
    mid = len(seq)//2
    pi = seq[mid]
    seq = seq[:mid] + seq[mid+1:]
    lo = [x for x in seq if x <= pi]
    hi = [x for x in seq if x > pi]
    return quick_sort(lo) + [pi] + quick_sort(hi)


q = quick_sort(s)
total =0
summer = 0
for i in q:
    summer+=i
    if summer>k:
        break
    total+=1













