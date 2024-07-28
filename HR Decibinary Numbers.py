
# Decibinary Numbers
# https://www.hackerrank.com/challenges/decibinary-numbers/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=dynamic-programming
"""

Check out ranges of 10
0-10
10-20
Etc..
See the pattern



"""

def toDecimal(x):
    s = str(x)
    total = 0
    counter = 0
    for i in range(len(s)-1,-1,-1):
        z = (2**counter)*int(s[i])
        total +=z
        counter+=1
    return(total)


dict = {}
#n = int(input())
for i in range(101):
    db = toDecimal(i)
    if db in dict:
        dict[db].append(i)
    else:
        dict[db] = [i]

for i in dict:
    print(dict[i],i)









