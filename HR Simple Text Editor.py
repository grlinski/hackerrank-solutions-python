


t = int(input())
s = ''

q = []
q.append(s)
for i in range(t):
    x = input()
    if x[0] == '1':
        z = q[-1]+x[2:]
        q.append(z)


    elif x[0] == '2':
        end = len(x[-1])-int(x[2:])
        z = q[-1][:end-1]
        q.append(z)


    elif x[0] == '3':
        pos = int(x[2:])-1

        print(q[-1][pos])


    elif x[0] == '4':
        del(q[-1])

    #print(t)
    #print(x)
    #print(q[-1])












