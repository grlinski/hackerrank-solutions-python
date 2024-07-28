

# https://www.hackerrank.com/challenges/two-characters/problem
# Two Characters


"""

For all letter pairs
Check to see if they alternate.
example
abcca
Doesn't work with a and c
as it would be acca

Maybe just make every pair beforehand


"""


from itertools import combinations


def createSequence(a,b,s):
    ns = ''

    for i in s:
        if i == a or i ==b:
            ns+=i

    return ns

def examineSequence(ns):
    for i in range(0,len(ns)-1):
        x = ns[i]
        y = ns[i+1]
        if x==y:
            return False
    return True








n = input()
s = input()
letters = set()
seq = []
for i in s:
    letters.add(i)
letters = list(letters)

pairs = []
for i in range(0,len(letters)-1):
    for j in range(i+1,len(letters)):
        a = letters[i]
        b = letters[j]
        pairs.append([a,b])


maxi = 0
for i in pairs:
    a = i[0]
    b = i[1]
    ns = (createSequence(a,b,s))
    if examineSequence(ns):
        #print(ns)
        maxi = max(maxi,len(ns))

print(maxi)

