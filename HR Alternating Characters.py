
# Alternating Characters
# https://www.hackerrank.com/challenges/alternating-characters/problem



def alternatingCharacters(s):
    n = ""
    ori = len(s)
    prev = 'x'
    for i in s:
        if i == prev:
            pass
        else:
            n=n+i
        prev = i
    q = ori - len(n)
    return q






q = 'ABABA'

print(alternatingCharacters(q))











