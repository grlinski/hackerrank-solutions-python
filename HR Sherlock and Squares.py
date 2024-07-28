


# Sherlock and Squares
# https://www.hackerrank.com/challenges/sherlock-and-squares/problem


# Amount of Square ints between and including a and b

import math

def squares(a, b):
    count=0
    first = 0
    firstgap = 0
    while (a <=b):

        j = int(math.sqrt(a))
        j = j**2
        if a == j and first == 0:
            first = a

            firstgap = ((math.sqrt(first))*2)+1
            while (a<=b):
                a = a+firstgap
                count+=1
                firstgap+=2
            return count


        a+=1

    return count


a = 3
b = 9

print(squares(a,b))






















