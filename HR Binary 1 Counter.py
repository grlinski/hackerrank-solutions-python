
# https://www.hackerrank.com/challenges/30-binary-numbers/problem



#x = int(input())
x = 5


b = bin(x)


b+='0'
count = 0
hicount = 0
for i in b:
    if i == '1':
        count+=1
    else:
        if count>hicount:
            hicount = count
        count=0



print(hicount)








