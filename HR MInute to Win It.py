
# Minute to Win It
# https://www.hackerrank.com/contests/w38/challenges/minute-to-win-it



"""

Array of n numbers
Find minmum amont of times required to change array

For all i from 1 to n-1
ai - ai-1 = k



Major Problem may be that first item is way off
Idea
Check consequtive values until getting the right difference, then go forward from there and backwards from there too.

There also may be different solutions for the same array.



Find the smallest point between numbers at the start and end
Example
Different list that start list
list1 = [1, 2, 5, 7, 9, 85, 13]

Check
1 and 13
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


"""


def minuteToWinIt(a, k):



    # Where to start from, both the end and beginning.
    fp = 0
    lp = len(a)-1
    cv = len(a)-1

    while True:
        first = a[fp]
        last = a[lp]

        checkval = (cv) * k

        print(fp, lp, cv, checkval)
        print(last-first)

        # Check if there is correct distance between first and last
        if (last-first) == checkval:
            break

        # Then decrease last and cv
        lp -=1
        cv -=1
        checkval = (cv) * k
        last = a[lp]

        print(fp, lp, cv, checkval)
        print(last - first)


        if (last-first) == checkval:
            break

        # Then decrease first and it will loop over
        lp-=1
        cv-=1



    # Most important Parts are fp and lp
    # These are the two values where I can jump from start to end

    print(fp,lp)
    print(first,last)

    # Probably Easiest to do it in sections.
    # Middle first, then start then end.
    # start = 0 to fp, fp to lp and lp to end
    # If it takes to long don't bother actually changing the values, just count misplaced values



    total = 0

    # Middle
    for i in range(fp,lp-1):
        cur = a[i]
        nex = a[i+1]
        if cur+k == nex:
            pass
        else:
            a[i+1] = cur+k
            total+=1

    # Start
    for i in range(0, fp-1):
        cur = a[i]
        nex = a[i + 1]
        if cur + k == nex:
            pass
        else:
            a[i + 1] = cur + k
            total += 1

    # End
    for i in range(lp, len(a)-1):
        cur = a[i]
        nex = a[i + 1]
        if cur + k == nex:
            pass
        else:
            a[i + 1] = cur + k
            total += 1



    #print(a)
    print(total)




list1 = [1, 1, 3, 4, 5, 6]
jump = 1


minuteToWinIt(list1,jump)





"""
Test Data
# Example Given
list1 = [1, 2, 5, 7, 9, 85]
jump = 2



list1 = [1, 2, 5, 7, 9, 85]
jump = 2


# Larger Data

list1 = [2, 3, 5, 7, 9, 85, 13, 14, 15]
jump = 2



list1 = [1, 1, 3, 4, 5, 6]
jump = 6


"""



















