



import math

# Winning Hand
# the product of the numbers on the cards mod a given value
# The modulo divisor is equal to another given value, the target value



import itertools

diction1 = {}



def winningHands(div, val, q):

    r= []
    for i in range(0,len(q)):
        x = q[i]%div
        if x == 0:
            pass
        else:
            r.append(x)

        for i in range(1,len(r)+1):
            print(list(itertools.combinations(r, i)))


#div = 8
#val = 2
#q = [2,2,2,3,4,5,6,7,8,9,10,10,11,12,14,16,12,3,35,46,12,12,53]


div = 3
val = 2
q = [2,2,2]


print(winningHands(div,val,q))
#print(diction1)






""" 
Create a new list where I divide every entry by the div value
Thus giving me the only part I care about.
Example, if div = 3, numbers like 3,6 or any multiple of 3 are useless.
Because 6%3 == 0
And many numbers are the same, example 4%3==0 as does 7%3




"""






