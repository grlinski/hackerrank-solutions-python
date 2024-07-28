

# The Love-Letter Mystery
# https://www.hackerrank.com/challenges/the-love-letter-mystery/problem




def theLoveLetterMystery(s):
    front = 0
    back = len(s)-1
    change=0
    if len(s) ==1:
        return 0

    for i in range(0,len(s)):
        x = ord(s[front])
        y = ord(s[back])

        # Break Condition
        if back <= front:
            break

        # Same
        if x == y:
            pass
        elif x > y:
            diff = x-y
            change = change+diff
            #x = x-diff
            #s[front] = chr(x)
        elif y > x:
            diff = y-x
            change = change+diff
            #y = y-diff
            #s[back] = chr(x)
        front +=1
        back -=1
    return change












s = 'cba'

print(theLoveLetterMystery(s))





