


# The Grid Search
# https://www.hackerrank.com/challenges/the-grid-search/problem

def gridSearch(g, p):
    gr = len(g)
    gc = len(g[0])

    pr = len(p)
    pc = len(g[0])

    fs = p[0]

    contains = False


    for i in range(0,gc):


        if i+pr > gc-1:
            break

        for j in range(0,gr):

            if j+len(fs) > gr:
                break
            s = g[i][j:j+len(fs)]
            #print(s)
            if s == fs:

                contains = True
                for n in range(0,pr):
                    px = p[n]
                    try:
                        gx = g[i+n][j:j+len(fs)]
                    except:
                        contains = False
                        break

                    if px == gx:
                        pass
                    else:
                        contains = False
                if contains == True:
                    return 'YES'


    if contains == True:
        return('YES')
    else:
        return('NO')









t = int(input())

for i in range(t):
    r,c = map(int, input().split(' '))
    g = []
    for j in range(r):
        s = input()
        g.append(s)
    r, c = map(int, input().split(' '))
    p = []
    for j in range(r):
        s = input()
        p.append(s)

    print(gridSearch(g,p))

















