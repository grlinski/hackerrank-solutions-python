
# Abbreviation
# https://www.hackerrank.com/challenges/abbr/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=dynamic-programming

"""
Capitalize Zero or more of string a's lowercase letters
Delete all of the remaining lowercase letters in a.
Can we make a into string b?



"""


def comparitor(a,b):
    apos = 0
    bpos = 0
    matches = 0

    while True:
        ax = a[apos]
        bx = b[bpos]
        al = ax.lower()
        bl = bx.lower()
        #print(ax,bx)
        if al==bl:
            matches+=1
            apos+=1
            bpos+=1
        elif al!=bl:
            if ax.islower():
                apos+=1
            else:
                return False
        if apos == len(a):
            if bpos!=len(b):
                return False
            else:
                return True
        if bpos == len(b):
            endpart = a[apos:]
            for i in endpart:
                if i.isupper():
                    return False
            return True








n = int(input())


for i in range(n):
    a = input()
    b = input()
    if comparitor(a,b):
        print('YES')
    else:
        print('NO')















