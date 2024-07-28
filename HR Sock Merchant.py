
# Sock Merchant

# https://www.hackerrank.com/domains/algorithms/implementation/2

"""

n = number of items
list of sock values


How many sock pairs can he sell?


9
10 20 20 10 10 30 50 10 20


"""

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
q = []
for i in range(0,max(ar)+1):
    q.append(0)

for i in ar:
    q[i]+=1
count = 0
x = 0
for i in q:
    if i !=0:
        print(i)
        x = int(i/2)
        print(x)
        count = count+x
print(count)




















