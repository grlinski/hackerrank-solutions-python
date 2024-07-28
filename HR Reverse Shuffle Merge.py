

# Reverse Shuffle Merge
# https://www.hackerrank.com/challenges/reverse-shuffle-merge/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=greedy-algorithms
"""


!!!!!!!!!!!!!!!!!!!!!!!!
Try and Figure tHis out quite hard




Given stringA
reverse = gives us the reverse of stringA
shuffle = denotes any string that is a full permutation of A
merge = merges A1 and A2 strings mainatining order of a strings characters.
However A1 and A2 can have their characters interspersed between them.

Ex:
A1 = 'abc'
A2 = 'def'
= abcdef

So we are given the end result of this

B = merge(reverse(A),shuffle(A))
So from B find what the lexicographically smallest A is.

So first demerge.
Both halves must have the same letters.
From this I can recreate reverse.






Notes:
abcdefgabcdefg

I can find out the last letter of the reverse
So for this I can tell it is a.
As after this the amount of a's I need to create a ==0.





"""

def createShuf(positions,dictLet,oriList):
    newB = ''
    for i in dictLet:
        amt = dictLet[i]//2
        newB+=i*amt
    print(newB)














dictLet ={}
positions = {}
b1 = input()
counter = 0
b = []
for i in b1:
    b.append(i)

for i in b:
    if i in dictLet:
        dictLet[i]+=1
    else:
        dictLet[i] = 1
    if i in positions:
        positions[i].append(counter)
    else:
        positions[i] = [counter]
    counter+=1

createShuf(positions,dictLet,b)







