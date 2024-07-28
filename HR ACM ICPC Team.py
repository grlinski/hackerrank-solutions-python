

#  ACM ICPC Team
# https://www.hackerrank.com/challenges/acm-icpc-team/problem



q = []
n,m = map(int, input().split(' '))

for i in range(0,n):
    x = int(input())
    q.append(x)



ans = []
dict = {}
maxik = 0
maxiv = 0

for i in range(0,n-1):
    for j in range(i+1,n):

        #print(i,j)

        x = len(str(q[i]+q[j]).replace('0',''))

        if x in dict:
            dict[x]+=1
            if x >= maxik:
                maxik = x
                maxiv = dict[x]


        else:
            dict[x]=1





print(maxik)
print(maxiv)


