
# Largest Permutation
# https://www.hackerrank.com/challenges/largest-permutation/problem
"""
Completed
What did I learn?
Well not a ton, just keep chugging away and use two dictionaries when num and pos are important





"""




n,k = map(int, input().split(' '))
list1 = list(map(int, input().strip().split(' ')))
numberd = {}
positiond = {}
aboveThisNumber = len
largestNumbers = []

def printAns(dict,n):
    for i in range(0,n):
        print(dict[i],end=" ")


def swapNumbers(numD,posD,n,k):
    largestNumber = n
    smallestNumber = 1
    position = 0
    while k > 0:
        if position > n:
            break
        if largestNumber == 0:
            break

        if largestNumber == posD[position]:
            position+=1
            largestNumber-=1
        else:
            smallNumber= posD[position]
            positionOfLargeNum = numD[largestNumber]


            posD[position] = largestNumber
            numD[largestNumber] = position
            posD[positionOfLargeNum] = smallNumber
            numD[smallNumber] = positionOfLargeNum

            k-=1
            largestNumber-=1
            position+=1


    return numD,posD


for i in range(0,len(list1)):
    positiond[i] = list1[i]
    numberd[list1[i]] = i

numberd, positiond = swapNumbers(numberd, positiond,n,k)


printAns(positiond,n)















