

# Min Max
# https://www.hackerrank.com/challenges/angry-children/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=greedy-algorithms

"""
This time I'll actually read the problem.
For Min Abs Diff I kinda jumped ahead and it caused a lot of problems.

Create an array of length k from elements of an array.
Such that it's unfairness is minimized
Call that array subarr
Unfairness is calculated as max(subarr)-min(subarr)


n
k
array

n = number of elements in the array
k = numbers in the subarray






Things I learned
Read the question fully, don't be an idiot and run ahead
Always check the edge cases
I had a problem with case 16 and this dealt with the last entries in the array.
Should have checked start,middle and end cases separately
Just make sure my loop goes through all items.





"""


n = int(input())
k = int(input())
list1 = []

for i in range(0,n):
    x = int(input())
    list1.append(x)

list1.sort()

ans = []
diff = 10000000000
print(list1)
for i in range(0,len(list1)-k):
    first = list1[i]
    ender = list1[i+k-1]
    if (ender - first) < diff:

        diff = ender-first
        ans = list1[i:i+k]
#print(ans)
print(diff)












