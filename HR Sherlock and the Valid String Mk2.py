

# Sherlock and the Valid String
# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
# MK1 mostly works, only wrong on a single case.
# Could fix it, but the code is very messy.
# Want to make it better.
# So here it is.
# This will pass most all cases, 14/20.
# I want a single loop to check for failures.


# Problems
# Need to see if there is a single 1 value in q.
# All other values must be equal.




s = input()
q = [0]*26
total=0
for i in s:
    x = ord(i)-97
    q[x]+=1
    total+=1

count = 0
for i in q:
    if i!=0:
        count+=1


freq =[]
for v in range(1,max(q)+1):
    x = q.count(v)
    if x!=0:
        freq.append(x)
print(freq)











