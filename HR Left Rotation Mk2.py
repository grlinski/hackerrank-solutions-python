


# Left Rotation
# https://www.hackerrank.com/challenges/array-left-rotation/problem


def rotLeft(t, list1):
    head = list1[:t]
    tail = list1[t:]
    ans = tail+head
    for i in ans:
        print(i,end=' ')









nums,t = map(int, input().split(' '))
list1 = list(map(int, input().rstrip().split()))



rotLeft(t,list1)












