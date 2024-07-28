

# HR Anagram
# https://www.hackerrank.com/challenges/anagram/problem



n = int(input())


def anagram(s):

    if len(s)%2!=0:
        return -1

    mid =len(s)//2
    s1 = s[:mid]
    s2 = s[mid:]
    letter = [0]*26

    let1 = [0] * 26
    let2 = [0] * 26

    for i in s1:
        let1[ord(i) - 97] += 1
    for i in s2:
        let2[ord(i) - 97] += 1

    total = 0
    for i in range(0, 26):
        total += abs(let1[i] - let2[i])
    return(total//2)



for i in range(n):
    s = input()

    print(anagram(s))













