

# HR Count Triplets Mk2
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

So that exists, however still not fast enough
Maybe create and store pairs, therefore I don't need to go over numbers again.
Do this for every entry.


Concept
2 2
1 2 1 2 4 4

So the seq is 1 2 4 obviously
But I'll store these sequences as pairs under a heading.
So for example 1 2 under the entry 4
4: [0,1]
However keep an entry for each number too
All the positions of 1s 2s, etc
So when I hit a middle value I try and create pairs.
Or rather really any number.
If I try and create a numbering system with 1 in the middle I won't get entries for a number lower than it.


So
every number enter their positions into a posDict
If this number divided by p has an entry in posDict create every pair possible, where x < y
Store all these pairs under the middle pairs heading in the middleDict
When I come across an end value do all the above and if it has a value/p entry in middle dict add up the lenth of that entry to total.

I don't actually need pairs, I just need amount of a value
If I get to a middle value all I need is the amount of the first value.


So far I no longer have problems with timeouts
Potential Problems
r/p == 1
Value errors, numbers not in the dict but I still try and use them




"""


n,p = map(int, input().split(' '))
list1 = list(map(int, input().strip().split(' ')))

total = 0
"""
Dictionaries
posDict, a listing of a number and all its positions
endSeq, key is the last value of a sequence, values are the first and second values of the sequence.
middleDict, key is the middle value of a sequence and all pairs it creates with the first value.

amt is just the amount of a number
Technically could just use posDict, but better to keep them seperate.
When I come across a middle value, all I need to do is see how many of the first number has already appeared.
Then 


"""
posSeq = {}
endSeq = {}
amt = {}
pairs = {}
middleValue = {}


for i in range(0,len(list1)):
    x = list1[i]
    #print(i)

    if x in posSeq:
        posSeq[x].append(i)
        amt[x]+=1
    else:
        posSeq[x] = [i]
        amt[x] = 1

    prev = x//p
    a = x
    b = int(x * p)
    c = int(x * p * p)
    #print(i,prev,a,b,c)
    if a in middleValue:
        if prev in amt:
            middleValue[a]+=amt[prev]
    else:
        if prev in amt:
            middleValue[a]=amt[prev]
        else:
            middleValue[a] = 0

    if c not in endSeq:
        endSeq[c] = [a,b]
    if a in endSeq:
        if prev in amt:
            total+=middleValue[prev]



if p == 1:
    total = 0
    for i in amt:
        if amt[i] >2:
            n = amt[i]-2
            tetra = (n*(n+1)*(n+2))/6
            total+=int(tetra)



#print(posSeq)
#print(amt)
#print(middleValue)
print(total)