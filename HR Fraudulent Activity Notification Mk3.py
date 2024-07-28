

# Fraudlent Activity Notification Mk2
# https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=sorting
"""

New approach for the portion of the list we are looking at use a dictionary.
For the entire portion maybe use a queue/deque.


del diction1[‘key’]



# Important Functions
dq = deque([1,2,3,4,5,6,'Billy'])
dq.append('bily')
dq.popleft()
dq.pop()
dq.appendleft('joe')


Counting Sort
https://www.youtube.com/watch?v=7zuGmKfUt7s





Also new idea
9 5
2 3 4 2 3 6 8 4 5

So I have a dictionary with the trailing expenditures
Now with a new item coming it and an old one leaving I need to change the median.
Assuming it's not the first time, we should have an old median.
However I can easily find the median based on what's coming and going

If a number higher than the previous median is coming in and a number lower than the previous median
The median won't change.
Equivalents will vary the change.
However two l






"""



def evenMedian(dict,d):
    medPos1 = (d//2)
    medPos2 = (d//2)+1




def oddMedian(dict,d):
    medPos = d//2+1
    total = 0
    median = 0
    for i in dict:
        total+=dict[i]
        if total>=medPos:
            median = i
            return median




#from collections import queue
from collections import deque

n,d = map(int, input().split(' '))
expend = list(map(int, input().strip().split(' ')))
expdq = deque(expend)
trailing = deque()

dict = {}

for i in range(0,d):
    x = expdq.popleft()
    trailing.append(x)
    if x in dict:
        dict[x]+=1
    else:
        dict[x]=1

even = False
if d%2 == 0:
    even = True
if even == True:
    median = evenMedian(dict,d)
else:
    median = oddMedian(dict,d)
    print(dict)
    print(median)

for i in range(0,len(expdq)-2):
    toAdd = expdq.popleft()
    toRem = trailing.popleft()
    trailing.append(toAdd)
    dict[toRem]-=1
    if dict[toRem] == 0:
        del(dict[toRem])
    if toAdd in dict:
        dict[toAdd]+=1
    else:
        dict[toAdd]=1

    if even == True:
        median = evenMedian(dict,d)
    else:
        median = oddMedian(dict,d)
        print(dict)
        print(median)

print(dict)
print(trailing)











