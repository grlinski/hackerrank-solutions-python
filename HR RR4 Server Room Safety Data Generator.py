
import random


# Generates Data Up to x amount
# Max is the max value it can be
# All ints
def data_gen(x,max):
    h = []
    p = []
    pset = set()

    while len(h) < x:
        y = random.randint(1, max)
        h.append(y)

    while len(pset) < x:
        y = random.randint(1,max)
        pset.add(y)

    p = list(pset)
    p.sort()

    return x,h,p
    # Each position must be greater than the one before it.


n, h, p = data_gen(10,100)
print('n =',n)
print('h =',h)
print('p =',p)









