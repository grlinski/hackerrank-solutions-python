

# Minimum Swaps 2
# https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays


n = int(input())

seq = list(map(int, input().strip().split(' ')))
# Seq: Pos
dict = {}
# Pos: Seq
dr = {}
for i in range(0,len(seq)):
    dict[seq[i]] = i+1
    dr[i+1] = seq[i]

total = 0

#print(dict)
#print(dr)

for i in range(1,len(seq)+1):
    #print(i)
    if dict[i] != i:

        holder = dict[i]
        holder2 = dr[i]
        print(holder, holder2)



        dict[i] = i
        dr[holder] = holder2
        dict[holder2] = holder
        total+=1
        #print(dict)




print(total)



"""
Alright I was pretty tired when I created this, so my writeup may be a bit messy as is the code.
So once we get the data I create 2 dictionaries. One called dict and dr, which is dictionary reversed.
So dict has the key:value pair as the actual sequence of numbers and its position. Note I started at 1 to make life easier.
1 5 4 2 3
Becomes, 1:1, 5:2, 4:3, 2:4 and 3:5
dr is the opposite, it stores the key:value pair the other way.
1:1, 2:5, 3:5, 4:3, 5:2
This is so I can easily know where the value is by referencing its position.
Anyways we go through a list of numbers from 1 to the sequence's length+1, using i
So if i doesn't equal the dict[i], it means the number is out of order and we need to swap.
Example:
For dict[1] = 1, So it's all good.
But dict[2] = 4, and we need to swap.

Swap
So to swap we store values first
holder = dict[i]
holder2 = dr[i]

The dict is essentially going to be our sorted list, so
dict[i] = i
I think we could skip this step, but it's not like it will take much time so whatever.
More important really is moving the misplaced value that the lower value overtakes.
Let me writeout an example
1 5 4 2 3

1 is in the correct position, so ignore.
We need to swap 5 and 2.
So from
dict[2] = 4
dict[5] = 2
dr..[4] = 2
dr..[2] = 5
to 
dict[2] = 2
dict[5] = 4

And that's what this does.
Store important values
holder = dict[i], h = 4
holder2 = dr[i], h2 = 5
dict[i] = i, dict[2] = 2, 2 is in the correct position
dr[holder] = holder2, dr[4] = 5, because 5 is now in the 4 position
dict[holder2] = holder, dict[5] = 4, because again 5 is in the 4 position
Remember that dict and dr are reverse of eachother.


I don't need to update the dr[2] key:values, as once we go through i=2, we never need to come back to this number.







"""



"""

Helpful Testcase I used to create my program

5
1 5 4 2 3

Swaps
1 5 4 2 3
1 2 4 5 3
1 2 3 5 4
1 2 3 4 5

First Swap is
5 and 2
Originally
Value, Position
dict[2] = 4
dict[5] = 2

dr..[4] = 2
dr..[2] = 4

Want to Change to
dict[2] = 2
dict[5] = 4

"""








