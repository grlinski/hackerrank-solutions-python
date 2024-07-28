

# Minimum Absolute Difference in an Array
# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=greedy-algorithms



x = int(input())

list1 = list(map(int, input().strip().split(' ')))


list1.sort()



diff = 1000
z = 0
for i in range(0, len(list1) - 1):
    x = list1[i]
    y = list1[i + 1]

    a = abs(x-y)
    b = abs(y-x)


    if a < diff:
        diff = a
    if b < diff:
        diff = b
print(diff)

