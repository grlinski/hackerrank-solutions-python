


# Taum and B'day
# https://www.hackerrank.com/challenges/taum-and-bday/problem
def taumBday(b, w, bc, wc, z):

    c1 = b*bc+w*wc

    c2 = b*(wc+z)+w*wc


    c3 = b*bc + w*(bc+z)

    return min(c1,c2,c3)





t = int(input())

for i in range(t):
    b,w = map(int, input().split(' '))
    bc,wc,z = map(int, input().split(' '))
    print(taumBday(b, w, bc, wc, z))









