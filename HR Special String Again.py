
# Special String Again
# https://www.hackerrank.com/challenges/special-palindrome-again/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=strings

"""
Basically count all palindrome substrings
This includes single characters
However I can just ignore those and add the length of the original string to my total.



Things I continue to be reminded of
Read the description!
Only the middle character can be different.
Compress things often makes it easier.







"""


def triangularNumber(x):
    tn = (x)*(x + 1) // 2
    return tn





def compressString(s):
    compS = []

    prev = s[0]
    s+='X'
    count = 1
    for i in range(1,len(s)):
        cur = s[i]
        if cur == prev:
            count+=1
        else:
            tup = (prev,count)
            compS.append(tup)
            prev = cur
            count = 1

    return(compS)


"""
How to count Palis
Single letters,
For each entry, get the triangular number of its occurance

Check if each entry is the middle of a palindrome.
If letters on either side are the same, then it is.
If the number letters of the same type are on both sides then continue to check.
If the number of letters differs there can be still be multiple palidromes formed.
Example, aabaaa, So with b the center
palis: b, aba, aabaa
When counting the amount of palis take the lower number.
This should be all I need.



"""



def checkMiddle(middle,mPos,mlet,mnum,cs):
    endGame = False
    total = 0
    pPos = mPos-1
    nPos = mPos+1

    while endGame!=True:
        prev = cs[pPos]
        plet = prev[0]
        pnum = prev[1]

        next = cs[nPos]
        nlet = next[0]
        nnum = next[1]

        if plet == nlet:
            if pnum == nnum:
                total+=pnum
            else:
                total+=min(pnum,nnum)
                endGame = True
        else:
            endGame = True
        pPos-=1
        nPos+=1
        if nPos == -1 or nPos == len(cs):
            endGame = True
    return total





def countPali(cs):

    total = 0
    middle = 'X'
    for i in range(0,len(cs)):
        cur = cs[i]
        let = cur[0]
        num = cur[1]
        total += triangularNumber(num)

        # Prev and Next
        if i-1 > -1 and i+1 < len(cs) and num ==1:
            prev = cs[i-1]
            plet = prev[0]
            pnum = prev[1]
            next = cs[i+1]
            nlet = next[0]
            nnum = next[1]
            if plet == nlet:
                total+=min(pnum,nnum)



    print(total)





n = int(input())
s = input()

cs = compressString(s)
countPali(cs)






















