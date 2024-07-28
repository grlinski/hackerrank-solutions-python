
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




"""




def lcs(a,b):
    r = len(a)+1
    c = len(b)+1
    rowC = []
    rowP = []

    rowC = [0]*r

    for i in range(1,r):
        x = a[i-1]
        rowP = rowC
        rowC = [0]

        for j in range(1,c):
            y = b[j-1]
            if x == y:
                v = rowP[j-1]+1
                rowC.append(v)
            else:
                v = max(rowP[j],rowC[j-1])
                rowC.append(v)
        print(rowC)
    print(rowC[-1])




a1 = input()
b1 = input()



if len(a1) > len(b1):
    a = a1
    b = b1
else:
    a = b1
    b = a1

lcs(a,b)

















