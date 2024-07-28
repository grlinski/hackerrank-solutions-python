
# Manasa and Stones
# https://www.hackerrank.com/challenges/manasa-and-stones/problem




def combos(n,a,b):

    mini = min(a,b)
    maxi = max(a,b)
    tmaxi = 0
    tmini = n-1

    if a == b:
        print((n-1)*a,end=' ')
    elif n == 1:
        print('0',end=' ')


    else:

        while tmini !=-1:
            ans = tmini*mini+tmaxi*maxi

            print(ans,end=' ')

            tmini-=1
            tmaxi+=1


t = int(input())

for i in range(t):
    n = int(input())
    a = int(input())
    b = int(input())
    combos(n,a,b)
    print()



























