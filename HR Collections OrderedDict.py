

# Collections OrderedDict
# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem


from collections import OrderedDict

dict = OrderedDict()

t = int(input())
for i in range(t):
    item, space, quantity = input().rpartition(' ')
    if item in dict:
        dict[item] += int(quantity)
    else:
        dict[item] = int(quantity)

for i in dict:
    print(i,dict[i])































