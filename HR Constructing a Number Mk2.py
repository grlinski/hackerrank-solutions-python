


# Sum all digits and Mod 3.

def canConstruct(x):
    total = 0
    for i in x:
        k = str(i)
        for j in k:
            total = total + int(j)

    if total%3 == 0:
        return 'Yes'
    else:
        return 'No'



cases = int(input())

for i in range(0,cases):
    items = int(input())
    q = input().split()
    ans = (sum_digits(q))
    if ans == 3 or ans == 6 or ans ==9:
        print('Yes')
    else:
        print('No')























