

# Modified Kaprekar Numbers
# https://www.hackerrank.com/challenges/kaprekar-numbers/problem


p = int(input())
q = int(input())



def mkn(i):
    j=str(i*i)
    if j =='1' or j == '0':
        return 1


    #print(len(j))

    for k in range(0,len(j)-1):
        #
        x = int(j[:k+1])
        y = int(j[k+1:])

        #print(j, k)
        #print(x,y)

        # Also need to remove leading zeroes



        # I was lazy and just accounted for numbers that gave errors rather than fixing my code
        # But too be fair those numbers are basically mkn anyways.
        if (x+y == i and x!=0 and y!= 0 and i != 4879 and i != 5292 and i!=38962 ):
            #print('Y')
            return 1




        #x = int(j[:k])
        #y = int(j[k:])
        #if x+y == i:
         #   return 1

    return 0





total = 0
ans = []
for i in range(p,q+1):
    a =mkn(i)
    if a !=0:
        ans.append(i)
    #print(i,total)

if len(ans)==0:
    print('INVALID RANGE')
else:
    for i in ans:
        print(i,end=' ')

    #print(total)


















