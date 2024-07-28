






# Security Involution Functions
# https://www.hackerrank.com/challenges/security-involution/problem

t = int(input())

s = list(map(int, input().strip().split(' ')))

invo = True

for i in range(0,len(s)):


    x = s[i]
    y = s[x-1]

    iy = s.index(y)

    if i+1 == y and x ==iy+1:
        pass
    else:
        invo = False
        #print(i,y,x,iy)

    #print(i+1,x,iy+1,y)

if invo == True:
    print("YES")
else:
    print('NO')


"""

i x
1 2

j y
2 1 

i x
2 1

j y
1 2 






"""



































