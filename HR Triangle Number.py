


# https://www.hackerrank.com/challenges/triangle-numbers/problem
# Triangle Numbers Mk2







def solve(x,dRow,dPos):

    if x in dPos:
        return dpos[x]
    row = [1]
    next = [1]
    print(row)
    x-=1


    for i in range(x):
        row = next
        row.insert(0, 0)
        row.insert(0, 0)
        row.append(0)
        row.append(0)
        next = []

        for k in range(1, len(row) - 1):
            h = row[k - 1] + row[k] + row[k + 1]
            next.append(h)


        dRow[i] = next
        print(dRow[i])

        for j in range(0, len(next)):
            if next[j] % 2 == 0:
                dPos[i] = j+1
                break


    return x,dRow,dPos










dRow = {}
dPos = {}
t = int(input())

solve(t,dRow,dPos)

new = int(input())
print(dPos[new])























