



# HR Sequence Equation
# https://www.hackerrank.com/challenges/permutation-equation/problem


"""
Explanation

5,2,1,3,4

So x is the position we are looking at, it goes through our list

Note that for this we need to start our list at 1 not 0.
So when x is at position 1 the value y is 5.
But for this we want the position of the actual 1 value that is somewhere in the list.
In this case it is at position 3.
So z = 3.
Now find the position of the value 3. Which is in spot 4.
That is the answer we are looking for.


If a number is in the correct location, there is no need to move it.


Simpler
list = [5,2,1,3,4]
x starts at 1, it is the original position
Value 1 is at position 3, find this.
Value 3 is at position 4, find this.
4 now is moved to position 1, for the answer list, not original.

x = 2.
Value 2 is in position 2. Can leave it be.

x = 3
Value 3 is at position 4.
Value 4 is at position 5.
5 is now in position 3 for the answer list.

x = 4
Value 4 is at position 5.
Value 5 is at position 1.
1 is moved to position 4 for the answer list.

x = 5
Value 5 is at position 1.
Value  is at posiiton 3.
3 is moved to position 5.

"""


#p = list(map(int, input().rstrip().split()))

p = [5,2,1,3,4]
dict1 = {}
dict2 = {}
ans = []
pos = 1
for i in p:
    dict1[i] = pos
    dict2[pos] = i
    pos+=1



for a in range(1,len(p)+1):

    b = dict1[a]
    c = dict1[b]
    print(c,end=' ')
    #print(a,b,c)
    #ans.append(c)

#print(ans)