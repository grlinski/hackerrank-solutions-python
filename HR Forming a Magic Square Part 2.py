# Forming a Magic Square
# https://www.hackerrank.com/challenges/magic-square-forming/problem


def sortout(list):
    x = list[0]
    y = list[1]
    z = list[2]
    print('agsdgs')
    xcont = x
    ycont = y
    zcont = z

    tdiff = 0
    lowestdiff = 10
    diffx = 0
    diffy = 0
    diffz = 0
    lx = 10
    ly = 10
    lz = 10

    # Ranges for Numbers
    rangexb = (1-x)
    rangext = (10-x)
    rangeyb = (1 - y)
    rangeyt = (10 -y)
    rangezb = (1 - z)
    rangezt = (10 - z)


    for i in range(rangezb,rangezt):
        for j in range(rangeyb,rangeyt):
            for k in range(rangexb,rangext):
                x = xcont+k
                y = ycont+j
                z = zcont+i

                if x+y+z == 15:
                    diffx = abs(x-xcont)
                    diffy = abs(y-ycont)
                    diffz = abs(z-zcont)
                    tdiff = diffx+diffy+diffz
                    if tdiff == 1:
                        return x,y,z
                    else:
                        lowestdiff = min(tdiff,lowestdiff)
                        if lowestdiff > tdiff:
                            lx = x
                            ly = y
                            lz = z



    print(x,y,z)
    print(lowestdiff)
    print(lx,ly,lz)


q = (3,9,1)
r = (5,6,9)
s = (3,3,3)
print(sortout(q))
print(sortout(r))
print(sortout(s))