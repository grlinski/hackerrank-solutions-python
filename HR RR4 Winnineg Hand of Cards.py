



import math

# Winning Hand
# the product of the numbers on the cards mod a given value
# The modulo divisor is equal to another given value, the target value

"""

input
n m x
num cards, modulo divisor, target value
Second Line
card values


""",


import itertools

diction1 = {}


def addtodict(x,div):
    y = x%div
    if y == 0:
        pass
    else:
        if y in diction1:
            diction1[y]+=1
        else:
            diction1[y] = 1


# n Choose k Combinations
def combinations(n, k):
    top = 1
    b1 = 1
    b2 = 1
    for i in range(1, n + 1):
        top = top * i
    for i in range(1, k + 1):
        b1 = b1 * i
    for i in range(1, n - k + 1):
        b2 = b2 * i
    answer = int(top / (b1 * b2))
    return answer



def multiply(x):
    total = 1

    for i in x:
        j = int(i)
        total = total*j
    return total

def onevalue(x,div,val):
    times= 0

    y = int(x[0])


    if y == val:
        times = times+diction1[y]

    amount = diction1[y]

    # Numy is used for choose permuations
    for i in range(2,amount+1):
        total = y**i

        if total%div == val:

            # Create an nCk function
            # n choose k

            r = combinations(amount,i)

            times+=r

    return times


def normalvalues(x):
    total = 1
    times = 1

    for i in x:
        j = int(i)
        total = total*j

        y = diction1[j]
        times = times*y

    return total,times





#n, div,val = (map(int, input().strip().split(' ')))
#q = input().split()



def winningHands(div, val, q):

    total = 0

    for i in q:
        addtodict(i,div)

    # Now we have our dictionary of keys, with the value being the amount.
    for i in range(1,len(diction1)+1):
        r = (list(itertools.combinations(diction1, i)))
        for j in r:
            if len(j) == 1:
                times = onevalue(j,div,val)
                if times!=0:
                    total+=times
            else:
                ans,times = normalvalues(j)
                if ans%div == val:
                    total+=times


    return(total)


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






