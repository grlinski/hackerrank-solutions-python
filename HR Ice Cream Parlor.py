
# Ice Cream Parlor
# https://www.hackerrank.com/challenges/icecream-parlor/problem




# Pick Index of costs that add to m
def icecreamParlor(m, c):
    dict = {}
    ans = ''

    h = -1
    doubles = False
    if m % 2 == 0:
        doubles = True
        h = m // 2
    d = []


    for i in range(0,len(c)):
        a = c[i]
        b = m-a






        if a == h and doubles == True:
            d.append(i+1)
            #print(d)
            if len(d)==2:
                #print(d[0],d[1])
                return d[0],d[1]

        elif a in dict:
            pass
        else:
            dict[a] = i+1

        if b in dict:
            print(a,b,m,dict[b],i)

            return dict[b],i+1







t = int(input())
for i in range(t):
    m = int(input())
    n = int(input())
    c = list(map(int, input().strip().split(' ')))
    a,b= (icecreamParlor(m,c))
    print(min(a,b),max(a,b))






