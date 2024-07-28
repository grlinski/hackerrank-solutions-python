


# HR Designer Door Mat
# https://www.hackerrank.com/challenges/designer-door-mat/problem



def control(n,m):


    boarder = (m-3)//2
    centerpeice = 1


    boarderfactor = -3
    centerpeicefactor = 2
    midpoint = ((n+1)//2)-1


    for i in range(n):

        if i == midpoint:
            boarderfactor = 3
            centerpeicefactor = -2

            cb = (m-7)//2
            print('-'*cb,end='')
            print('WELCOME',end='')
            print('-'*cb)



        else:

            print('-'*boarder,end='')
            print('.|.'*centerpeice,end='')
            print('-' * boarder)


        boarder+=boarderfactor
        centerpeice +=centerpeicefactor










#n,m = map(int,input().split(' '))
n = 7
m = 21
control(n,m)


















