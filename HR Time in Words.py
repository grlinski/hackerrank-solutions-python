


# Time in Words
# https://www.hackerrank.com/challenges/the-time-in-words/problem



h = int(input())
m = int(input())


num = ['twelve','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve']



num2 = ['zero','one','two','three','four','five','six','seven','eight','nine','ten',
        'eleven', 'twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty',
        'twenty one','twenty two','twenty three','twenty four','twenty five','twenty six','twenty seven','twenty eight','twenty nine','thirty']



if m > 30:
    m2 = 30 -(m%30)

else:
    m2 = m
#print(m%30)
hour = num[h]
minute = num2[m2]



ans = ''
first = ''
second = ''
if m==0:
    ans += hour +' o\' clock'
elif m == 15:
    ans += 'quarter past '+hour
elif m == 30:
    ans += 'half past ' + hour
elif m == 45:
    ans += 'quarter to ' +num[h+1]
elif m == 1:
    ans += minute +' minute past ' +hour
elif m == 59:
    ans += minute + ' minute to ' +num[h+1]
elif m < 30:
    ans += minute +' minutes past ' +hour
elif m > 30:
    ans += minute +' minutes to ' +num[h+1]



print(ans)



