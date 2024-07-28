
# Group Groups and Groupdict
# https://www.hackerrank.com/challenges/re-group-groups/problem


import re

pattern = re.compile(r'(\w)\1+')
s = input()

y = pattern.search(s)
try:
    item2 = (y.group(1))
    print(item2)
except:
    print(-1)









