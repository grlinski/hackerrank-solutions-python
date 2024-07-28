

# Find Digits
# https://www.hackerrank.com/challenges/find-digits/problem


def findDigits(n):
    count = 0
    s = str(n)
    for i in s:
        if i == '0':
            pass
        else:
            x = int(i)
            if n%x==0:
                count+=1
    return count







q = 10121
print(findDigits(q))
















