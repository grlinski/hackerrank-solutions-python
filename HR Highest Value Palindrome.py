
# Highest Value Palindrome
# https://www.hackerrank.com/challenges/richie-rich/problem
"""
Remember to change middle number if len is odd
And there is enough of k to do so

Okay there are 3 types of changes
a and b both aren't 9.
Either change both to 9 or change one to the other
a or b is nine
Simply change one of them to 9.
I mainly need to calculate how many of each I can do.
As I want mostly 9s but I may not have enough changes to do so.






"""

def printAns(dict,n):
    for i in range(0,n):
        print(dict[i],end=" ")



def swapValues(posD,diffs,nineDiff,leng,k,s):

    niners = k-diffs
    print(nineDiff)
    print(niners)
    print(diffs)

    j = len(s) - 1

    for i in range(0, len(s) // 2):
        a = posD[i]
        b = posD[j]



        j -= 1




    print('n,k',niners,k)

    return posD





n,k = map(int, input().split(' '))
s = input()
j = len(s)-1
leng = len(s)
# Note these dicts, key = name, value = other
numD = {}
posD = {}
differences = 0
nineDifference = 0
for i in range(0,len(s)//2):
    a = s[i]
    b = s[j]
    if a!=b and a!='9' and b!='9':
        differences+=1
    elif a!=b:
        nineDifference+=1
    posD[i] = a
    posD[j] = b

    j-=1


posD = swapValues(posD,differences,nineDifference,leng,k,s)



print(posD)
print(differences)
print(leng)
printAns(posD,leng)

















