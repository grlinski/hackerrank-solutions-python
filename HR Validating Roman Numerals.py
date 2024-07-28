
# Validating Roman Numerals
# https://www.hackerrank.com/challenges/validate-a-roman-number/problem


"""
Cannot have multiple V or L or D
Only C I and X

(C|X|I){0,3}
(D|L|V|)

((C|X|I){0,3}|(D|L|V|))




"""


import re

pattern = re.compile(r'((M|C|X|I){0,3}|(D|L|V|))((M|C|X|I){0,3}|(D|L|V|))((M|C|X|I){0,3}|(D|L|V|))((M|C|X|I){0,3}$|(D|L|V|)$)')


pattern = re.compile(r'((M){0,3}|(D|C|L|X|V|I))((C){0,3}|(D|L|X|V|I))')


pattern = re.compile(r'((M){0,3}|(D|C|L|X|V|I))(D)')




x = 'CCCVXX'

item1 = input()

y = pattern.search(item1)
item2 = (y.group())
if item2 == item1:
    print('TRUE')
else:
    print('FALSE')













