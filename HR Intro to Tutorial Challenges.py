# https://www.hackerrank.com/challenges/tutorial-intro/problem
# Intro to Tutorial Challenges



"""

Input
v the value that has to be searched
n = array size
ar n numbers that make up the array




"""


def introTutorial(V, arr):
    for i in range(0,len(arr)):
        if arr[i] == V:
            return i





V = int(input().strip())
n = int(input().strip())
arr = list(map(int, input().strip().split(' ')))
result = introTutorial(V, arr)
print(result)




















