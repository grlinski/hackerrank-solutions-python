

# Common Child
# https://www.hackerrank.com/challenges/common-child/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

# Check out
# https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
# Note strings are same length to start.


s = input()
r = input()

a = []
b = []
m = [[0]*len(s)]*len(s)

for i in range(len(s)):
    a.append(s[i])
    b.append(r[i])


print(a,b)


print(m)














