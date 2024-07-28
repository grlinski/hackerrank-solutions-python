


# HR Equalize the Array
# https://www.hackerrank.com/challenges/equality-in-a-array/problem



n = int(input())
a = list(map(int, input().rstrip().split()))
dict = {}

for i in a:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1

maxi = 0
for i in dict.keys():
    maxi=max(maxi,dict[i])

if maxi == 1:
    print(len(a)-1)
else:
    print(len(a)-maxi)







