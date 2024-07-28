


# Making Anagrams
# https://www.hackerrank.com/challenges/making-anagrams/problem




s1 = input()
s2 = input()

let1 = [0]*26
let2 = [0]*26


for i in s1:
    let1[ord(i)-97]+=1
for i in s2:
    let2[ord(i) - 97] += 1

#print(let1)
#print(let2)

total = 0
for i in range(0,26):
    total += abs(let1[i] -let2[i])
print(total)


