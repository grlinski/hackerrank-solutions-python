

#from itertools import accumulate
# Array Manipulation
# https://www.hackerrank.com/challenges/crush/problem

"""
There was a good explanation in the discussion
Basically I don't need to add the value to every item in the range.
I just need to add it to the start and subtract it from the end.
This is more like an index of where values start and stop.
So at the end when we sum things up it's more like record of where values were added.
And anything after that will contain that change.
However anything after will not, so we subtract the value.


Mini Example
n = 5
So we need an array with 6 spots, 
Because if we need to add a number to spot 5, we also need to show that any number outside that range doesn't recieve that change

q = 0 0 0 0 0 0
So now the operations
Where a,b,c, a is the start of the range, b is the end and c is the added value.
1 2 1
1 0 -1 0 0 0
So we added c to the start, a and subtracted it from the position after b, ie b+1
We could test this now to see if things work.
So positions 1 and 2 have a value of 1. All other spots have a value of 0.
Starting at position 1, it has a value of 1.
Keeping a running total, we add the value of p2 which is 0.
So position 2 has a value of 1.
P3 is -1, so add that to the running total, which is 0.
P3 = 0, as does the rest of the array.
Try one more.
2 5 3
1 3 -1 0 0 -3
a +=3, and b+1 -=3
Now if we did a running total, we'd see that the max value we obtain is 4 at position 2.




"""



n,ops = map(int, input().split(' '))

# Note, I am lazy and added an unused section in the list.
# I prefer to work with lists starting from 1, makes positioning easier
# So this has an unused zero spot
# It also has a spot at the end which is used but goes beyond the operation ranges.
# This is however used
q = [0]*(n+2)


#print(q)
for i in range(ops):
    a,b,k = map(int, input().split(' '))

    q[a]+=k
    q[b+1]-=k


total = 0
ans = 0

for i in q:
    total = total+i
    if total > ans:
        ans = total
print(ans)


#print(max(accumulate(q)))


















