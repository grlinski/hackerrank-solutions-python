
# Diagonal Differences
import math
n = 3
a = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

rightdiag = 0
leftdiag = 0
adder = 0
subber = n-1

for i in range(0,len(a)):
    x = a[i]
    rightdiag = x[adder]+rightdiag
    leftdiag = x[subber]+leftdiag
    adder +=1
    subber-=1

answer = abs(rightdiag-leftdiag)
print(answer)






















