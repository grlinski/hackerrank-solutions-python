

# Common Child
# https://www.hackerrank.com/challenges/common-child/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=strings
"""

Checkout V2 Mk2 for a completed version




V2 had promise but I'm more interested in my way.

However I'm already stalled and now back on V2




"""


def compressString(s):
    compS = []
    set1 = set()

    prev = s[0]
    s+='X'
    count = 1
    for i in range(1,len(s)):
        cur = s[i]
        set1.add(cur)
        if cur == prev:
            count+=1
        else:
            tup = (prev,count)
            compS.append(tup)
            prev = cur
            count = 1
    return(compS,set1)

# This Ignores Letters not in SetA
def compressStringB(s,setA):
    compS = []
    set1 = set()

    prev = s[0]
    s+='X'
    count = 1
    for i in range(1,len(s)):
        cur = s[i]
        set1.add(cur)
        if cur == prev:
            count+=1
        else:
            tup = (prev,count)
            if prev in setA:
                compS.append(tup)
            prev = cur
            count = 1
    return(compS,set1)




a = input()
b = input()
a,seta = compressString(a)
b,setb = compressStringB(b,seta)



print(a)
print(b)




























