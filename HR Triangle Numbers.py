
# HR Triangle Numbers
# https://www.hackerrank.com/challenges/triangle-numbers/problem


def solve(x):
    # Keyvalue
    kv = x


    prev =[0,0,1,0,0]

    for i in range(1,x+1):
        q = []


        for j in range(2,(i*2)+1):

            y = prev[j-2]+prev[j-1]+prev[j]

            if i == kv and y != 0 and y%2 == 0:
                return int(j)-1

            q.append(y)

        #print(q)
        q.append(0)
        q.append(0)
        q.insert(0,0)
        q.insert(0,0)

        prev = q














t = int(input())

for i in range(t):
    x = int(input())
    print(solve(x))











