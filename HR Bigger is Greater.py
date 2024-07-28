

# Bigger is Greater
# https://www.hackerrank.com/challenges/bigger-is-greater/problem

def biggerIsGreater(w):
    swap = False
    q = []
    for i in w:
        q.append(ord(i))
        #print(ord(i)-96)

    pivot = 0
    for i in range(0,len(q)-1):
        x = q[i]
        y = q[i+1]
        if y > x:






    if swap == False:
        print('no answer')
    else:
        s=''
        for i in q:
            s+=chr(i)
        print(s)




t = int(input())

for i in range(0,t):
    s = input()
    biggerIsGreater(s)










