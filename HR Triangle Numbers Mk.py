
# https://www.hackerrank.com/challenges/triangle-numbers/problem
# Triangle Numbers


rowEvenPos = {}





def solve(x,row):

    next = []
    x -= 1
    row.insert(0,0)
    row.insert(0, 0)
    row.append(0)
    row.append(0)



    for i in range(1,len(row)-1):
        h = row[i-1]+row[i]+row[i+1]
        next.append(h)

   # print(next)

    if x == 0:
        for i in range(0,len(next)):
            if next[i]%2 == 0:
                return i+1
    else:
        return solve(x,next)




t = int(input())
t-=1
row = [1]
print(row)

x = (solve(t,row))
print(x)




