


# Strange Grid
# https://www.hackerrank.com/challenges/strange-grid/problem


r,c = map(int, input().split())

# Max 5 Columns

rowbin = (r+1)%2

# Column Number
c = (c-1)*2+rowbin
r = ((r-1)//2)*10


print(c+r)












