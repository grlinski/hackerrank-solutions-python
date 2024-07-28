
# The Maximum Subarray
# https://www.hackerrank.com/challenges/maxsubarray/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign



def maxArray(s):
    maxEven = 0

    # Since I skip over zeroes a lot, may as well check if there is one
    zero = False
    total = 0

    if s[0] <0:
        neg = True
    else:
        neg = False

    q = []

    for i in range(0,len(s)):
        x = s[i]
        if x == 0:
            zero = True

        if x <0 and neg == True:
            total+=x
        elif x < 0 and neg == False:
            q.append(total)
            neg = True
            total = x
        elif x > 0 and neg == False:
            total+=x
        elif x > 0 and neg == True:
            q.append(total)
            neg = False
            total = x






        # Evens ignore this as it works.
        if x >0:
            maxEven+=x
    q.append(total)
    q.append(None)
    print(q)

    if q[0] < 0:
        q = q[1:]
    if q[0] == None:
        return None

    x = 0
    y = 0
    total = 0
    ans = []
    for i in range(0,len(q)):
        x = q[i]
        y = q[i+1]
        if y == None:
            break
        else:
            if x+y > 0:
                total += x+y
            else:
                ans.append(total)
                total=0
    ans.append(total)
    maxi = max(ans)
    print(maxi)


    #return maxEven







t = int(input())

for i in range(t):
    throw = input()
    s = list(map(int, input().strip().split(' ')))



    (maxArray(s))




















