
# https://www.hackerrank.com/challenges/insertionsort1/problem
# Insertion Sort Part 1

"""


input
size of array
array


"""

def insertionSort1(n, arr):
    q = []
    size = len(arr)-1
    for i in range(size,0,-1):
        if arr[i] < arr[i-1]:

            holder  = arr[i]
            arr[i] = arr[i-1]
            for k in arr:
                print(k,end=" ")
            arr[i-1] = holder
            print()
    for k in arr:
        print(k, end=" ")















n = int(input().strip())
arr = list(map(int, input().strip().split(' ')))
insertionSort1(n, arr)

















