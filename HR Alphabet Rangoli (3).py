





# HR Designer Door Mat
# https://www.hackerrank.com/challenges/designer-door-mat/problem



def print_rangoli(s):

    if s == 0:
        print ('')
    elif s == 1:
        print('a')
    else:



        fb = (s-1)*2
        eb = (s-1)*2-1

        start = 96+s

        firstletters = 1
        endletters = 0

        letterfactor = 1




        boarderfactor = -2

        midpoint = (s -1)
        #print(midpoint)



        for i in range(s*2-1):

            if i == midpoint:
                for a in range(0,firstletters):
                    x = chr(start-a)
                    print(x,end='')
                    print('-',end='')
                for a in range(endletters,0,-1):
                    x = chr(start-a+1)
                    print(x,end='')
                    if x == chr(start):
                        pass
                    else:
                        print('-',end='')
                print()





                boarderfactor = 2
                letterfactor = -1



            else:
                print('-'*fb,end='')

                for a in range(0,firstletters):
                    x = chr(start-a)
                    print(x,end='')
                    print('-',end='')
                for a in range(endletters,0,-1):
                    x = chr(start-a+1)
                    print(x,end='')
                    print('-',end='')

                print('-'*eb)

            fb+=boarderfactor
            eb+=boarderfactor
            firstletters +=letterfactor
            endletters +=letterfactor
















#n,m = map(int,input().split(' '))
s = 1
print_rangoli(s)


































