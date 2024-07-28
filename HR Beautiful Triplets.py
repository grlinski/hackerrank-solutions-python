

# Beautiful Triplets
# https://www.hackerrank.com/challenges/beautiful-triplets/problem



n,d = map(int, input().split(' '))

q = list(map(int, input().strip().split(' ')))
total = 0
for i in range(len(q)-2):
    a = q[i]

    for j in range(i+1,len(q)-1):
        b = q[j]
        if b-a > d:
            break

        for k in range(j+1,len(q)):

            if b-a != d:
                break
            c = q[k]
            if c-b == d:
                #print(a,b,c)
                total+=1
            if c-b > d:
                break

print(total)























