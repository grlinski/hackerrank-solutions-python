


# https://www.hackerrank.com/challenges/no-idea/problem
# No Idea



"""

Like A
Dislike B


Input
Number of Ints and then A/B Length
Array of Ints
Set A
Set B




"""



def no_idea(arr,a,b):
    happ = 0
    for i in arr:
        if i in a:
            happ+=1
        elif i in b:
            happ-=1
    return happ




"""

a = input().split()
a = list(map(int, a))




"""




n = 0
m = 0
arr = [1,5,3]
a = {3,1}
b = {5,7}











