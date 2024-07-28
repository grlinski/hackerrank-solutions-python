

# Detect HTML Tags
# https://www.hackerrank.com/challenges/detect-html-tags/problem

import re


def detectTags(x,setter):
    pattern = re.compile(r'^<[a-z]+(>|\s)')
    y = pattern.findall(x)


    for i in y:
        j = str(i)
        if j[0] == '<':
            j = j[1:]
        if j[-1] == '>':
            j = j[0:-1]
        print(j)
        setter.add(j)


def sortSet(setter):
    list1 = list(setter)
    list1.sort()
    ans = ''
    for i in list1:
        ans = i+';'
    print(ans[:-1])




x = '<head> <p >'
#x = input()
setter = set()
detectTags(x,setter)


"""
Tags
<html
<head >
<p>

So starts with <
Ends with either > or whitespace
(<).+(>|\w)







"""























