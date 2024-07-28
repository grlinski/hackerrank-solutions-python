

# Maximizing XOR
# https://www.hackerrank.com/challenges/maximizing-xor/problem




a = int(input())
b = int(input())
b+=1


maxi = 0
for i in range(a,b):
    for j in range(a,b):
        q = (i ^ j)
        maxi = max(maxi,q)

print(maxi)








