
# Compress the String
# https://www.hackerrank.com/challenges/compress-the-string/problem



x = input()

count = 1
prev = x[0]
x = x+'A'

for i in range(1,len(x)):
    cur = x[i]
    if cur == prev:
        count+=1
    else:
        print('('+str(count)+',',str(prev) +')',end=' ')
        count = 1
        prev = cur







