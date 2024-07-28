

# Max Array Sum
# https://www.hackerrank.com/challenges/max-array-sum/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=dynamic-programming
"""

Could do this in sets of 5

i-2,i-1,i,i+1,i+2
if I pick i it has no impact on i-2 or i+2




"""
n = input()
s = list(map(int, input().strip().split(' ')))

minList = []

for i in range(0,len(s)):
    if i ==0:
        x = s[i]-s[i+1]
    elif i == len(s)-1:
        x = s[i]-s[i-1]
    else:
        x = s[i]-s[i-1]-s[i+1]
    minList.append(x)

"""
Go through minList
See if a number is larger than both its neighbours.
If so choose it and skip the next neighbour.
Also check original list to make sure the number isn't negative.

Problem is if the numbers are equal

"""

total =0
i = 0


print(minList)

while True:
    cur = minList[i]
    next = minList[i+1]

    if i == len(minList)-2:
        picker = max(s[i],s[i+1])
        if picker>0:
            total+=picker
        break


    if cur>next and s[i]>0:
        total+=s[i]
        i+=2
    else:
        i+=1

    #print(total,cur,next,i)



    if i>=len(minList)-1:
        break



print(total)






























