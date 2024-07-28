

# Find the Median
# https://www.hackerrank.com/challenges/find-the-median/problem



def quick_sort(seq):
    if len(seq) < 2 : return seq
    mid = len(seq)//2
    pi = seq[mid]
    seq = seq[:mid] + seq[mid+1:]
    lo = [x for x in seq if x <= pi]
    hi = [x for x in seq if x > pi]
    return quick_sort(lo) + [pi] + quick_sort(hi)




def findMedian(arr):

    seq = quick_sort(arr)
    leng = len(seq)

    if leng%2==0:
        m1 = seq[leng//2]
        m2 = seq[(leng//2)-1]
        return (m1+m2)//2
    else:
        return seq[((leng-1)//2)]








n = int(input())

s = list(map(int, input().strip().split(' ')))

print(findMedian(s))


