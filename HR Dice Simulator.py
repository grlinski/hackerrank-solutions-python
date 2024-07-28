

# Not Really an HR program, but will help with a problem
# https://www.hackerrank.com/challenges/s10-mcq-1/problem


# Mostly just for interest

# Simulate two die rolls a certain amount of times and print out how often a number appears.

import random

spread = [0]*11
print(spread)

for i in range(0,100000):
    x = random.randint(0, 5)
    y = random.randint(0, 5)
    spread[x+y]+=1

total = sum(spread)
for i in range(len(spread)):
    print('Number: ', i+2, round(spread[i]/total*100,1))







