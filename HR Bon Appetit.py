

# https://www.hackerrank.com/challenges/bon-appetit/problem

"""

Anna doesn't eat any of the kth items
Where 0 < K < n
Anna and Brian split the bill
However Anna didn't eat the kth item


input
n, k . n = number of items ordered, k = item anna didn't eat
cost of n items
what anna was charged for her bill


Was Anna charged correctly?
If so print Bon Appetit
Else print what she should be refunded




"""

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())


total = 0
correct_bill_anna = 0
for i in ar:
    total = total+i
correct_bill_anna = int((total -ar[k])/2)

if correct_bill_anna == b:
    print('Bon Appetit')
else:
    x = b-correct_bill_anna
    print(x)













