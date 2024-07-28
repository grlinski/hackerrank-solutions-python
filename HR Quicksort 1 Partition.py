
# QuickSort 1 Partition
# https://www.hackerrank.com/challenges/quicksort1/problem



size = int(input())
s = list(map(int, input().strip().split(' ')))


left = []
right = []
equal = []
pivot = s[0]
for i in range(0,len(s)):
    if s[i] > pivot:
        right.append(s[i])
    elif s[i] < pivot:
        left.append(s[i])
    elif s[i] == pivot:
        equal.append(s[i])

arr = left+equal+right
print(arr)
