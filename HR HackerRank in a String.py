
# HackerRank in a String
# https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem


def hackerrankInString(s):
    ans = 'hackerrank'
    # 10 Letters/Positions 0-9
    anspos = 0
    count = 0

    for i in s:
        x = ans[anspos]
        if i == x:
            anspos+=1
            count+=1
        if count == 9:
            return "YES"


    return "NO"







s = 'hereiamstackerrank'
q = 'hackerworld'


print(hackerrankInString(s))
print(hackerrankInString(q))











