
# Validating Phone Numbers
# https://www.hackerrank.com/challenges/validating-the-phone-number/problem



import re
pattern = re.compile(r'(7|8|9)\d\d\d\d\d\d\d\d\d')

t = int(input())
for i in range(t):
    item1 = input()

    y = pattern.search(item1)
    if y == None:
        print('NO')
    else:
        item2 = y.group()
        if item1 == item2:
            print('YES')
        else:
            print('NO')









