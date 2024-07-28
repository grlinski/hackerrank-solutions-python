
# Common Child
# https://www.hackerrank.com/challenges/common-child/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=strings
"""
Same = Diagonally+1
Not same == max of Left or Up







Should work on all cases just too slow
Don't use an entire matrix
Just keep the previous row and current Row
And then Prev Row will be overwritten the the Cur row when I move down.
Problems with unequal string lengths




Can't pass timelimit on 9-13
How to optimize???
Maybe only have a single Row
Gotta think this over with pen and paper.
Store Prev Diagonal


Now passes all by 9 and 12
With the cleancode function however it passes all but 10,11,13

Now only 9 and 13...
Now latest 9,11,12


Next idea is to shorten b as I go along
Maybe if I get 5 of the same in a row chop everything before that.
Example
[0, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
Since I have 5 3s in a row, chop out 0,1,2
However need to have a large difference
Meaning I need to store the largest value I've encounted so far.




Completed
What I learned
Sometimes the tried and true way is best, I learned the basic algorithm via youtube
Then I hugely optimized it.
Removed the grid, used a single line array and a few variables.
This gave me close to the answer but I needed more.
I then created a tolerance system, at 10% the longest string length.
This could lead to incorrect answers but is unlikely.
Basically I could start to ignore portions of my array if I keep getting the same values over and over.
Meaning nothing much is changing or changing at too slow a rate and is unlikely to influence the end result.
Therefore best to skip over these and focus on the important sections.
Check out the Previous 5 section.





"""




def lcs(a,b):
    r = len(a)+1
    c = len(b) + 1
    rowC = []

    rowC = [0]*c
    #print(r,c)
    counter = 0
    cStart = 1
    hiVal = 0

    tolerance = 0.1*len(a)

    for i in range(1,r):
        x = a[i-1]
        curV = rowC[cStart-1]
        prevD = curV



        for j in range(cStart,c):
            y = b[j-1]
            prevDStorage = rowC[j]
            if x == y:
                v = prevD+1
                rowC[j] = v
                curV = v

                # Previous 5
                if j > 5 and curV+tolerance<  hiVal:
                    p1 = rowC[j-1]
                    p2 = rowC[j-2]
                    p3 = rowC[j-3]
                    p4 = rowC[j-4]
                    if p1==p2 and p2 == p3 and p3==p4:
                        cStart+=4
            else:

                v = max(rowC[j],curV)
                rowC[j] = v
                curV = v
            if curV > hiVal:
                hiVal = curV
            prevD = prevDStorage

        #print(rowC)
    print(rowC[-1])



def cleanStrings(a,b):
    seta = set()
    setb = set()
    a1 = ''
    b1 = ''

    for i in a:
        seta.add(i)
    if len(seta) == 26:
        return a,b
    for i in b:
        if i in seta:
            b1+=i
        else:
            setb.add(i)
    if setb == seta:
        return a,b1
    for i in a:
        if i not in setb:
            a1+=i

    return a,b


a1 = input()
b1 = input()

a1,b1 = cleanStrings(a1,b1)


if len(a1) > len(b1):
    a = a1
    b = b1
else:
    a = b1
    b = a1
#a,b = padding(a,b)
#print(len(a))
#print(len(b))

lcs(a,b)






"""


AAABANXJTISKAJVBBBASASFASFASAA
BSAAAAJVUAASDKASGIASOGIJAOISGJOAISGNS


ans = 15

"""










