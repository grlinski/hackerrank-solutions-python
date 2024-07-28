
# Forming a Magic Square
# https://www.hackerrank.com/challenges/magic-square-forming/problem


def sortout(list):
    x = list[0]
    y = list[1]
    z = list[2]

    xcont = -9
    ycont = -9
    zcont = -9

    while x+y+z != 15:
        for i in range(-8,8):
            for j in range(-8,8):
                for k in range(-8,8):
                    x = x+i
                    y = y+j
                    z = z+k
    print(x,y,z)


q = (1,9,4)
sortout(q)







def formingMagicSquare(s):
    r1 = s[0]
    r2 = s[1]
    r3 = s[2]

    while sum(r1)!=15:
        x = r1[0]
        y = r2[1]
        z = r3[2]







    return change

s = []
for s_i in range(3):
   s_t = [int(s_temp) for s_temp in input().strip().split(' ')]
   s.append(s_t)
result = formingMagicSquare(s)
print(result)

"""

4 8 2
4 5 7
6 1 6


"""







