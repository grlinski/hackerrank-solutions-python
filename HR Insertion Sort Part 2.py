

# Insertion Sort Part 2
# https://www.hackerrank.com/challenges/insertionsort2/problem


"""

6
1 4 3 5 6 2


"""


def insertionSort2(n, arr):
    for i in range(1,len(arr)):
        x = arr[i]
        y = i-1
        while y >=0:
            if x < arr[y]:
                arr[y+1] = arr[y]
                arr[y] = x
                y = y-1
            else:
                break
        for k in arr:
            print(k,end= " ")
        print()














n = int(input().strip())
arr = list(map(int, input().strip().split(' ')))
insertionSort2(n, arr)


"""
7
7 1 3 5 9 2 3



"""







