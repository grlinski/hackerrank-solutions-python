

# Lonely Integer
# https://www.hackerrank.com/challenges/lonely-integer/problem



n = int(input())
q = list(map(int, input().strip().split(' ')))



freq = []
for v in range(0,max(q)+1):
    x = q.count(v)
    freq.append(x)
for i in range(0,len(freq)):
    if freq[i] == 1:
        print(i)











