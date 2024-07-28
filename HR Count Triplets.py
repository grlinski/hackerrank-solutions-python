

# HR Count Triplets
# https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=dictionaries-hashmaps



"""
With a sequence of numbers get the amount of triplets that follow a geometric progression
a,b,c
Order matters, but they don't have to directly follow eachother.

Idea
for every number create a progression sequence.

Example
prog = 3

if a number is 2
make (2,6,18) and store it.
Also store how many 2s there are.


Numbers may not actually be in order
Therefore this makes it loads harder
Maybe only check the ending value.

Example
where p == 2

1 2 2 4
So when I start at 1 create a seq 1,2,4, store this under 4.
So then check if 4 is in end value sequences
Since it is then check how many numbers for the rest of the seq exist.
Ignore how many times 4 appears, since I'm only concerened about this particular 4.
So I'd get 2 total.


Also I just realized my new approach doesn't account for unordered numbers.

Example
p = 2
2 1 4
This would still count as a hit since when we get to 4 it doesn't account for the position of 2 or 1
Instead of the amounts, keep positions of a number
so 2 appears at 0
2:0
Then when getting to 4 and checking endSeq check all entries of 1 and 2
Create all pairs of positions of 1s and 2s.
All pairs that have lower values of 1 then 2 are added to the total.

Careful where p/R == 1
Probably do entire different function for that

"""

# Want amount of number pairs, where a is lower
"""
Concept Faster Way about this
Example
a = 1 2 3 4 5 6 7
b = 4 5 6 7 8
I can just stop when I see that 1 is less than 4.
total +=len(b), or rather do it for whatever is left of b

Gets tricky when I get to something like 4
Note for my example it doesn't actually make sense since there can't be two 4s.
But whatever.
So then when I hit a==4 , I ignore all b's until I hit a number greater than 4.
And so on.




"""
def countAmount(a,b):
    total = 0
    for i in a:
        for j in b:
            if i < j:
                total+=1
    return total



n,p = map(int, input().split(' '))
list1 = list(map(int, input().strip().split(' ')))
dSeq = {}

endSeq = {}
positions = {}


total = 0
curPos = 0

for i in list1:

    if i in positions:
        positions[i].append(curPos)
    else:
        positions[i] = [curPos]

    if i in endSeq:
        es = endSeq[i]
        a = es[0]
        b = es[1]
        counter = 0
        if a not in positions or b not in positions:
            pass
        else:
            a = positions[a]
            b = positions[b]
            counter = countAmount(a,b)
            total+=counter
    a = i
    b = int(i*p)
    c = int(i*p*p)
    if c not in endSeq:
        endSeq[c] = (a,b,c)
    curPos+=1

print(total)