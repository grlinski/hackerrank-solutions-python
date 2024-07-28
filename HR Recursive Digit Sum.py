

# Recursive Digit Sum
# https://www.hackerrank.com/challenges/recursive-digit-sum/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=recursion-backtracking
#
def digitalRoot(x):
    total = 0
    for i in x:
        y = int(i)
        total+=y
    return str(total)

num,times = map(str, input().split(' '))
t = int(times)

for i in range(t):
    num = digitalRoot(num)
    print(num)
print(num)


