
import math
x = input()
list1 = list(map(int, input().strip().split(' ')))

lowest = list1[0]
highest = list1[0]
highcount = 0
lowcount = 0


del(list1[0])

for i in list1:

    if highest < i:
        highest = i
        highcount +=1
    if lowest > i:
        lowest = i
        lowcount += 1



print(highcount,lowcount)









































