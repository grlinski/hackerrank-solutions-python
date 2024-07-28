

# Funny String
# https://www.hackerrank.com/challenges/funny-string/problem

import math


def funnyString(s):
    r = s[::-1]

    for i in range(0,len(s)-1):
        x = ord(s[i])
        y = ord(s[i+1])
        z = abs(x-y)

        a = ord(r[i])
        b = ord(r[i+1])
        c = abs(a-b)

        if z!=c:
            return 'Not Funny'
    return 'Funny'











s = 'acxzgg'
print(funnyString(s))






















