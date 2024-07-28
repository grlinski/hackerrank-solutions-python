
# Fraudlent Activity Notification Mk2
# https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=sorting

"""
2x greater than or equal to the clients median spending for a trailing amount of days
Need to have at least that trailing number of prior days transaction data

Given trailing days d and a clients total expenditure for n days
Find the number of times the client will recieve a notification over all n days


Example
d = 3
expenditures 10,20,30,40,50
So for the first 3 days we just track data, since d = 3.
So on day 4, check previous 3 days data.
median is 20, don't include day 4 in this yet.
Since 40 >= 20x2 send a notice.
Then again at day 5
Previous 3 days are 20,30,40, median = 30
50 < 30x2 so don't send a notice.


Going to Need to Use Queues
Check out the .py file





"""


def evenMedian(list1,d):
    mid1 = (d//2)
    mid2 = (d // 2) + 1
    ans = (list1[mid1]+list1[mid2])/2
    return ans

def oddMedian(list1,d):
    mid = (d//2)
    return(list1[mid])

def addRemove(toAdd,toRem,list1):
    if toAdd == toRem:
        return list1
    list1.remove(toRem)
    for i in range(0,len(list1)):
        cur = list1[i]
        if i == 0 and toAdd <= cur:
            list1.insert(0,toAdd)
            return list1
        elif i == len(list1)-1 and toAdd >= cur:
            list1.append(toAdd)
            return list1
        elif toAdd == cur:
            list1.insert(i, toAdd)
            return list1
        else:
            prev = list1[i-1]
            if toAdd > prev and toAdd < cur:
                list1.insert(i, toAdd)
                return list1




def checkNotification(list1,d,cur):
    if d%2 ==0:
        median = evenMedian(list1,d)
    else:
        median = oddMedian(list1,d)

    #print('Cur, Median')
    #print(cur,median)
    if cur >= median*2:
        return True
    else:
        return False





n,d = map(int, input().split(' '))
expend = list(map(int, input().strip().split(' ')))

trailing = expend[:d]
trailing.sort()

notifications = 0

# Do inital notification check here.
if checkNotification(trailing,d,expend[d]):
    notifications+=1


for i in range(d+1,len(expend)):
    cur = expend[i]
    toRem = expend[i-d-1]
    toAdd = expend[i-1]
    #print('Times',i)
    #print('Trailing')
    #print(trailing)
    #print('Add,Rem,Cur')
    #print(toAdd,toRem,cur)
    trailing = addRemove(toAdd,toRem,trailing)
    #print('New Trailing')
    #print(trailing)

    if checkNotification(trailing, d, cur):
        notifications += 1

print(notifications)








