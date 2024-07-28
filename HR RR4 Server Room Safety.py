


# Server Room Safety
# https://www.hackerrank.com/contests/rookierank-4/challenges/server-room-safety


# Check Which Sides are not Protected


def checkAll(n,h,p):

    # If there is a break in continuation set to True
    rightgap = False
    leftgap = False

    rend = False
    lend = False

    for i in range(0,len(p)):

        cur = h[i]

        # Check the Ends
        if i == 0:
            prev = cur
            lend = True
        else:
            prev = h[i - 1]
            lend = False

        if i == len(p)-1:
            nex = cur
            rend = True
        else:
            nex = p[i + 1]
            rend = False

        # Right, Current to Next
        if rend == False:
            hitright = cur - (abs(p[i] - p[i+1]))
        else:
            hitright = 0

        if hitright >= 0 or rend == True:
            pass
        else:
            #print(cur,nex)
            rightgap = True

        # Left, Current to Prev
        hitleft = cur - (abs(p[i] - p[i -1]))


        # Left Previous to Current
        if hitleft >=0 or lend == True:
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
p = [1,2,3,4,8]
p2 = [1,2,3,4,5]
h = [1,1,1,1,1]


print(checkAll(n,h,p))
