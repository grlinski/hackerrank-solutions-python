
# Detect HTML Tags
# https://www.hackerrank.com/challenges/detect-html-tags/problem

# Seems to Work but doesn't pass all testcases
# I'm not getting headers for some reason
# Completed, forgot that headers contain numbers


import re


def detectTags(x,setter):
    pattern = re.compile(r'(<[a-z]+\s)|(<[a-z\d]+>)')
    y = pattern.findall(x)

    #print(y)
    for i in y:
        for j in i:
            j = j.strip('>')
            j = j.strip('<')
            j = j.strip(' ')
            setter.add(j)
    return setter


def sortSet(setter):
    list1 = list(setter)
    list1.sort()
    ans = ''
    for i in list1:
        ans = ans+i+';'
    print(ans[1:-1])


t = int(input())
set1 = set()

for times in range(t):
    x = input()
    set1 = detectTags(x, set1)

sortSet(set1)


"""
Tags
<html
<head >
<p>

So starts with <
Ends with either > or whitespace
(<).+(>|\w)







"""


































