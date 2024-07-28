
# Fraudlent Activity Notification
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







"""


def evenMedian(list1,d):
    mid1 = (d//2)
    mid2 = (d // 2) + 1
    ans = (list1[mid1]+list2[mid2])/2
    return ans

def oddMedian(list1,d):
    mid = (d//2)+1
    return(list1[mid])

def addRemove(toAdd,toRem,list1):
    removed = False
    added = False
    if toAdd == toRem:
        return list1


    newList = []
    pos = 0
    while pos < len(list1):
        x = list1[pos]

        if x == toRem and removed == False:
            list1 = list1[:pos]+list1[pos+1:]
            removed = True
            pos-=1

        if pos == 0:
            if toAdd <= list1[pos] and added == False:
                list1 = [toAdd]+list1
                added = True
        elif pos == len(list1)-1 and added == False:
            if toAdd >= list1[pos]:
                list1.append(toAdd)
                added = True
        else:
            prev = list1[pos-1]
            next = list1[pos+1]
            if toAdd == prev or toAdd == next or (toAdd > prev and toAdd < next):
                list1 = list1[:pos]+[toAdd]+list1[pos:]
                added = True
        if added == True and removed == True:
            break
        pos+=1


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








