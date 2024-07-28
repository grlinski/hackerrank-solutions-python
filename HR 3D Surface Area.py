
# Basically I have to create and then find the area of a 3D object.
# Mainly based on height.
"""

Important points.
The top and bottom surface will always be h*w and then double it
Since there's no zeroes.
This leaves 4 other sizes.
Each cube is then determined by its neighbours.
Maybe add zeroes to all sides.

NESW sides
URDL sides


"""

def cubeSizes(i,j,cubes):

    # Surface Area total
    sa = 0

    x = cubes[i][j]
    up = cubes[i-1][j]
    dn = cubes[i+1][j]
    lf = cubes[i][j-1]
    rt = cubes[i][j+1]

    # Sides
    if x-up >0:
        sa+=(x-up)
    if x-dn >0:
        sa+=(x-dn)
    if x-lf >0:
        sa+=(x-lf)
    if x-rt >0:
        sa+=(x-rt)

    #print(x,sa)

    return sa







h,w = map(int, input().split(' '))

cubes = []
zeroes = [0]*(w+2)
cubes.append(zeroes)
for i in range(h):
    x = list(map(int, input().strip().split(' ')))
    x = [0]+x+[0]
    cubes.append(x)

cubes.append(zeroes)
#print(cubes)

total = 0
for i in range(1,h+1):
    for j in range(1,w+1):
        #print(cubes[i][j])
        total += cubeSizes(i,j,cubes)


top = h*w
btm = h*w

#print(total)
#print(top,btm)
print(total+top+btm)








"""

3 3
1 3 4
2 2 3
1 2 4

"""

