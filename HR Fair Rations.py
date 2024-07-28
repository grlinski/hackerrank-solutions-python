

# Fair Rations

# https://www.hackerrank.com/challenges/fair-rations/problem




n = int(input())
q =  list(map(int, input().strip().split(' ')))


summer = sum(q)
total=0
odds = 0
evens = 0

for i in range(0,len(q)-1):


    a = q[i]
    b = q[i+1]

    if a%2 ==0:
        pass
    elif a%2 !=0:
        q[i]+=1
        q[i+1]+=1
        total+=2



if summer%2!=0:
    print('NO')
else:
    print(total)























"""
Rules
Every time you give a loaf of bread to some person i, you must also give a loaf of bread to the person 
immediately in front or behind them in line
Either i+1 or i-1

Once all the bread is distributed each person must have an even number of loaves.


"""


