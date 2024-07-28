# https://www.hackerrank.com/challenges/maximum-draws/problem


# Actually Called Maximum Draws

"""

Input is first the amount of cases
Then each is the number of total pairs of socks in the drawer
Assuming each pair is distinct
Worst case scenario how many socks do we need to remove to get a matching pair?

I'm guessing basically this is numberofsocks/2+1



2
1
2



"""


n = int(input())
list1 = []

for i in range(0,n):
    line = input()
    list1.append(line)

for i in list1:
    x = int(i)+1
    print(x)















































