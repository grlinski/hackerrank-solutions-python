
# HR Maximum Element
# https://www.hackerrank.com/challenges/maximum-element/problem


t = int(input())
q = []


largest = []
total = 0
items = 0
maxi = 0

for i in range(t):
    x = list(map(int, input().strip().split(' ')))

    if x[0] == 1:
        q.append(x[1])


        if x[1] >= maxi:
            largest.append(x[1])
            maxi = x[1]
        elif items <=50:
            largest.append(x[1])



    elif x[0] == 2:

        rem = q[-1]
        try:
            largest.remove(q[-1])
        except:
            pass
        if rem == maxi:
            try:
                maxi = max(largest)
            except:
                maxi = 0
        del(q[-1])


    else:
        print(maxi)



