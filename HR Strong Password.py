

# Strong Password
# https://www.hackerrank.com/challenges/strong-password/problem

import re
n= int(input())
s = input()



nm = "0123456789"
lc = "abcdefghijklmnopqrstuvwxyz"
uc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sc = "!@#$%^&*()-+"


nt = 1
lt = 1
ut = 1
st = 1

for i in s:
    if i in nm:
        nt = 0
    if i in lc:
        lt = 0
    if i in uc:
        ut = 0
    if i in sc:
        st = 0



total = nt+lt+ut+st


if total + n < 6:
    total +=6-(total+n)
    print(total)
else:
    print(total)












