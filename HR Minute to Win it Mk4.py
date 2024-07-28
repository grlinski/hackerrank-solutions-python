






# Minute to Win It
# https://www.hackerrank.com/contests/w38/challenges/minute-to-win-it

"""
1+13 = 14
14//jump = 7
7%len = 0 so it works

Pick a start and end value then work from there

Make sure forumula works

Example
Jump = 3
4 7 10 13 16 19 22

(Last - First)
22 - 4 = 18
This number shoud equal jump * (len-1)



There is a single problem,
On 3 testcases it is off by +1
So either it'll pass all but those 3 or only pass those 3
So my program is occassionally doing one more process than needed.



"""


def minuteToWinIt(a, k):
    total = 0
    b = []
    c = []
    d = []
    e = []

    for i in a:
        b.append(i)
        c.append(i)
        d.append(i)
        e.append(i)



    """
    for i in range(len(a)-1,0,-1):
        cur = a[i]
        prev = a[i-1]

        if cur-prev == k:
            pass
        else:
            a[i-1] = cur-k
            total+=1
    """


    s1 = 0
    s2 = 1
    s3 = 2
    s4 = 3
    s5 = 4
    for i in range(0,len(a)-1):

        #S1
        cur1 = a[i]
        nex1 = a[i+1]

        if cur1-nex1 == k:
            pass
        else:
            a[i+1] = cur1-k
            s1+=1

        #S2
        try:
            cur2 = b[i+1]
            nex2 = b[i+2]

            if cur2-nex2 == k:
                pass
            else:
                b[i+2] = cur2-k
                s2+=1
        except:
            pass

        #S3
        try:
            cur3 = c[i + 2]
            nex3 = c[i + 3]

            if cur3 - nex3 == k:
                pass
            else:
                c[i + 3] = cur3 - k
                s3 += 1
        except:
            pass


        #S4
        try:
            cur4 = d[i + 3]
            nex4 = d[i + 4]

            if cur4 - nex4 == k:
                pass
            else:
                d[i + 4] = cur4 - k
                s4 += 1
        except:
            pass

        #S5
        try:
            cur5 = e[i + 4]
            nex5 = e[i + 5]

            if cur5 - nex5 == k:
                pass
            else:
                e[i + 5] = cur5 - k
                s5 += 1
        except:
            pass
    print(s1,s2,s3,s4,s5)
    return min(s1,s2,s3,s4,s5)








list1 = [1, 2, 5, 7, 9, 85, 13]
jump = 2


print(minuteToWinIt(list1,jump))





"""
Test Data
# Example Given
list1 = [1, 2, 5, 7, 9, 85,13]
jump = 2



list1 = [1, 2, 5, 7, 9, 85]
jump = 2


# Larger Data

list1 = [2, 3, 5, 7, 9, 85, 13, 14, 15]
jump = 2



list1 = [1, 1, 3, 4, 5, 6]
jump = 6



# Everything is wrong
list1 = [1,2,4,5,6,7,8,1,12,4,2,5,3,6,1,2,15]
jump = 27
# Works


# First digits are wrong
list1 = [80,70,80,634,1241, 11,13,15,17,19,21,23,25,27]
jump = 2

list1[1,3,5,7,9,11,13,15,17,19,21,23,25,27]





"""



















