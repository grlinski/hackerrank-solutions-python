


# Server Room Safety
# https://www.hackerrank.com/contests/rookierank-4/challenges/server-room-safety




# Forgot that a really tall stack can reach others multiple positions away.
# Need a keep track of the current stack with the largest reach
# However this reach will decrease as we go right.

# Start only doing the right side reach
# Just reverse h and p to do left side
# Check Which Sides are not Protected


def checkAll(n,h,p):

    # If there is a break in continuation set to True
    rightgap = False
    leftgap = False

    high = 0
    highr = 0

    h.append(0)
    h.insert(0,0)
    p.append(0)
    p.insert(0,0)


    pr = p[::-1]
    hr = h[::-1]

    """
    print(h)
    print(p)
    print(hr)
    print(pr)
    """

    for i in range(1,len(p)-1):

        # Going Right
        high = high - abs(p[i]-p[i-1])
        cur = h[i]
        high = max(high,cur)
        nex = h[i+1]

        # Added padding to the ends, if both pos and height  == 0 skip.
        if nex == 0 and p[i+1] ==0:
            hitright = 0
        else:
            hitright = high - (abs(p[i] - p[i + 1]))
            if hitright >=0:
                pass
            else:
                #print(high,nex,hitright,i)
                rightgap = True




        #Right Checker Values
        """
        print('Num',i)
        print('CurH',high,p[i])
        print('Next',h[i+1],p[i+1])
        print(hitright)
        print(rightgap)
        """


        # Going Left, Uses the Reverse Lists
        highr = highr - abs(pr[i] - pr[i - 1])
        curr = hr[i]
        highr = max(highr, curr)
        nexr = hr[i + 1]

        # Added padding to the ends, if both pos and height  == 0 skip.
        if nexr == 0 and pr[i + 1] == 0:
            pass
        else:
            hitleft = highr - (abs(pr[i] - pr[i + 1]))
            if hitleft >= 0:
                pass
            else:
                leftgap = True

        if leftgap == True and rightgap == True:
            return 'NONE'




    if leftgap == True and rightgap == True:
        return 'NONE'
    elif leftgap == True:
        return 'LEFT'
    elif rightgap == True:
        return 'RIGHT'
    else:
        return 'BOTH'




n = 5
p2 = [1,2,3,4,8]
p = [1,2,3,4,5]
h = [1,1,1,1,1]


print(checkAll(n,h,p))

n = 4
h = [10,6,5,2]
p = [1,3,5,6]

#print(checkAll(n,h,p))