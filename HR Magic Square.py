

# Forming a Magic Square
# https://www.hackerrank.com/challenges/magic-square-forming/problem
import random


def formingMagicSquare(s):
    change = 0

    r1 = sum(s[0])
    r2 = sum(s[1])
    r3 = sum(s[2])
    c1 = s[0][0]+s[1][0]+s[2][0]
    c2 = s[0][1] + s[1][1] + s[2][1]
    c3 = s[0][2] + s[1][2] + s[2][2]
    # Use these rows and cols to determine where the problems are
    # Ex: if r1 and c2 are wrong the problem is at position 2
    #Positions

    ender = r1+r2+r3

    while (ender)!= 45:


    # Row 1
        if r1 != 15 and c1 != 15:
            x = s[0][0]
            y = sum(s[0]) - x
            z = 15-y
            s[0][0] = z
            change = change+(abs(z-x))
        elif r1 != 15 and c2 != 15:
            x = s[0][1]
            y = sum(s[0]) - x
            z = 15-y
            s[0][1] = z
            change = change+(abs(z-x))
        elif r1 != 15 and c3 != 15:
            x = s[0][2]
            y = sum(s[0]) - x
            z = 15-y
            s[0][2] = z
            change = change+(abs(z-x))

        # Row 2
        elif r2 != 15 and c1 != 15:
            x = s[1][0]
            y = sum(s[1]) - x
            z = 15-y
            s[1][0] = z
            change = change+(abs(z-x))
        elif r2 != 15 and c2 != 15:
            x = s[1][1]
            y = sum(s[1]) - x
            z = 15-y
            s[1][1] = z
            change = change+(abs(z-x))
        elif r2 != 15 and c3 != 15:
            x = s[1][2]
            y = sum(s[1]) - x
            z = 15-y
            s[1][2] = z
            change = change+(abs(z-x))

        # Row 3
        elif r3 != 15 and c1 != 15:
            x = s[2][0]
            y = sum(s[2]) - x
            z = 15-y
            s[2][0] = z
            change = change+(abs(z-x))
        elif r3 != 15 and c2 != 15:
            x = s[2][1]
            y = sum(s[2]) - x
            z = 15-y
            s[2][1] = z
            change = change+(abs(z-x))
        elif r3 != 15 and c3 != 15:
            x = s[2][2]
            y = sum(s[2]) - x
            z = 15-y
            s[2][2] = z
            change = change+(abs(z-x))


        r1 = sum(s[0])
        r2 = sum(s[1])
        r3 = sum(s[2])
        c1 = s[0][0] + s[1][0] + s[2][0]
        c2 = s[0][1] + s[1][1] + s[2][1]
        c3 = s[0][2] + s[1][2] + s[2][2]
        ender = r1+r2+r3


    print(s)
    return change














data1 = [[4, 9, 2], [3, 5, 7], [8, 1, 7]]
data2 = [[4, 8, 2], [4, 5, 7], [6, 1, 6]]


data2 = [[4, 8, 2], [4, 5, 7], [6, 1, 6]]


r = []
for i in range(0,3):
    q = []
    a = random.randint(1, 9)
    q.append(a)
    a = random.randint(1, 9)
    q.append(a)
    a = random.randint(1, 9)
    q.append(a)
    r.append(q)


print(r)
print(formingMagicSquare(r))



"""
Problems with high numbers
data5 = [[8, 4, 5], [3, 8, 9], [9, 6, 1]]
[[6, 4, 5], [-2, 8, 9], [8, 6, 1]]
8


"""








