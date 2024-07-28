


# HR Game of Thrones 1
# https://www.hackerrank.com/challenges/game-of-thrones/problem


s = input()

leng = len(s)


letter = [0]*26
for i in s:
    letter[ord(i)-97]+=1



if leng ==1:
    print('YES')

elif leng%2==0:
    pali = True
    for i in letter:
        if i%2!=0:
            pali = False
            break
    if pali == True:
        print('YES')
    else:
        print('NO')
else:
    pali = True
    oneodd = 0
    for i in letter:
        if i%2!=0:
            oneodd+=1

    if oneodd !=1:
        print('NO')
    else:
        print('YES')

























