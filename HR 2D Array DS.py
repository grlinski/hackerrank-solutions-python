

q = []
for i in range(0,6):

    x = list(map(int, input().strip().split(' ')))
    q.append(x)



maxi = -100000
for r in range(0,4):
    for c in range(1,5):

        # Hour Glass
        # Starting From Left Top
        tl = q[r][c-1]
        tc = q[r][c]
        tr = q[r][c+1]

        mm = q[r+1][c]

        bl = q[r+2][c-1]
        bc = q[r+2][c]
        br = q[r+2][c+1]

        total = (tl+tc+tr+mm+bl+bc+br)
        maxi = max(total,maxi)



print(maxi)













