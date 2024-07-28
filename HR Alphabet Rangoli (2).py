

# a == 97

# HR Alphabet Rangoli

# https://www.hackerrank.com/challenges/alphabet-rangoli/problem


t = int(input())
size = t*2+1
startval = 96+t

# Startboarder
sb = t+1



for i in range(size):
    print('-'*sb)
    for j in range(0,t):
        print(chr(97+j)+'-')
    print('-'*(sb-1))





