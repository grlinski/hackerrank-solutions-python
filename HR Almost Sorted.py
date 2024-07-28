



def problemArea():
    pass


n = int(input())
s = list(map(int, input().strip().split(' ')))
prev = -1


nProbs = 0
problem = False
pA = []


inStart = 0
inEnd = 0


swap1 = 0
swap2 = 0

anchor = -1






for i in range(0,len(s)):
    cur = s[i]

    if cur > prev and problem == False:
        prev = cur
    elif cur < prev and problem == False and nProbs == 0:
        anchor = prev
        pA = [prev, cur]
        prev = cur
        problem = True
        nProbs+=1
        inStart = i-1
        swap1 = i-1

    elif problem == True and nProbs == 1:
        if cur > prev:
            problem = False
            inEnd = i-1
        elif cur < prev:
            pA.append(cur)
        prev = cur
    elif nProbs > 0:
        nProbs+=1
        swap2 = i
        prev = cur

# Small Lengths


if len(s) == 2:
    if s[1] > s[0]:
        print('yes')
    else:
        print('yes')
        print('swap 1 2')
elif len(s) == 3:
    if s[2] > s[1] and s[1] > s[0]:
        print('yes')
    elif s[0] > s[1] and s[0] > s[2] and s[2] > s[1]:
        print('no')
    elif s[1] > s[2]:
        print('yes')
        print('swap 2 3')
    elif s[0] > s[2]:
        print('yes')
        print('swap 1 3')
    elif s[0] > s[1]:
        print('yes')
        print('swap 1 2')

elif nProbs > 2:
    print('no')
elif nProbs ==2:
    print('yes')
    print('swap',swap1+1,swap2+1)
elif nProbs ==1:
    print('yes')
    print('reverse',inStart+1,inEnd+1)
elif nProbs == 0:
    print('yes')


"""
print('End')
print(pA)
print(inStart,inEnd)
print(swap1,swap2)
print(nProbs)
"""

"""

6
1 5 4 3 2 6



"""