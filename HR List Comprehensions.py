


x = 1
y = 1
z = 1

n = 2


ans = []
for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
            if i+j+k != n:
                q = [i,j,k]
                ans.append(q)


print(ans)













