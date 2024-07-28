



# Encryption
# https://www.hackerrank.com/challenges/encryption/problem



import math


sx = input()

s = sx.replace(' ','')
print(s)

x = len(s)

r = math.floor(math.sqrt(x))
c = math.ceil(math.sqrt(x))



breaker = 0
pos = 0
sp = 0
while True:


    if breaker == len(s):
        break


    print(s[pos],end='')
    pos+=c
    if pos>=len(s):
        sp+=1
        pos = sp
        print(' ',end='')
    breaker+=1












