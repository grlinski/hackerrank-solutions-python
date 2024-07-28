



# Max Array Sum
# https://www.hackerrank.com/challenges/max-array-sum/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=dynamic-programming
"""

Things I learned
This was actually quite easy
I just needed to think simply and think through the problem



"""


n = input()
s = list(map(int, input().strip().split(' ')))

# Sort these three first
back3 = s[0]
back2 = s[1]
back1 = s[2]
if back3 < 0:
    back3 =0
if back2 < 0:
    back2 = 0
if back1 < 0:
    back1 = 0
back1 = back1+back3
s[2] = back1


for i in range(3,len(s)):
    x = s[i]
    if x <= 0:
        x = 0
    back2 = s[i-2]
    back3 = s[i-3]
    maxi = max(back2,back3)
    ans = x+maxi
    s[i] = ans

print(max(s[-1],s[-2]))























































